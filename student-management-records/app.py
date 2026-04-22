from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func
from models import db, User, Student, Attendance, Mark
from datetime import datetime
import os
from uuid import uuid4

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

SUBJECTS = [
    ('english', 'English'),
    ('mathematics', 'Mathematics'),
    ('science', 'Science'),
    ('social_studies', 'Social Studies'),
    ('computer_science', 'Computer Science')
]

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def get_students_in_alphabetical_order():
    return Student.query.order_by(
        func.lower(func.trim(Student.name)),
        func.length(func.trim(Student.roll_no)),
        func.lower(func.trim(Student.roll_no))
    )


def generate_temporary_roll_no():
    return f"TMP-{uuid4().hex[:10].upper()}"


def recalculate_student_roll_numbers():
    students = get_students_in_alphabetical_order().all()

    for student in students:
        student.roll_no = f"TMP-{student.id}"

    db.session.flush()

    for index, student in enumerate(students, start=1):
        student.roll_no = f"{index:03d}"

    db.session.flush()


def build_marks_lookup(students):
    student_marks = {}

    for student in students:
        student_marks[student.id] = {mark.subject: mark.marks for mark in student.marks}

    return student_marks

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def dashboard():
    if current_user.role == 'student':
        student = Student.query.filter_by(user_id=current_user.id).first()
        students = [student] if student else []
    else:
        students = get_students_in_alphabetical_order().all()
    return render_template('dashboard.html', students=students)

@app.route('/students')
@login_required
def students():
    if current_user.role not in ['admin', 'teacher']:
        return redirect(url_for('dashboard'))
    students = get_students_in_alphabetical_order().all()
    return render_template('students.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
@login_required
def add_student():
    if current_user.role != 'admin':
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        name = request.form['name']
        class_ = request.form['class']
        email = request.form['email']
        phone = request.form['phone']
        student = Student(
            name=name,
            roll_no=generate_temporary_roll_no(),
            class_=class_,
            email=email,
            phone=phone
        )
        db.session.add(student)
        db.session.flush()
        recalculate_student_roll_numbers()
        db.session.commit()
        flash('Student added successfully')
        return redirect(url_for('students'))
    return render_template('add_student.html')

@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_student(id):
    if current_user.role != 'admin':
        return redirect(url_for('dashboard'))
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.class_ = request.form['class']
        student.email = request.form['email']
        student.phone = request.form['phone']
        recalculate_student_roll_numbers()
        db.session.commit()
        flash('Student updated successfully')
        return redirect(url_for('students'))
    return render_template('edit_student.html', student=student)

@app.route('/delete_student/<int:id>')
@login_required
def delete_student(id):
    if current_user.role != 'admin':
        return redirect(url_for('dashboard'))
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.flush()
    recalculate_student_roll_numbers()
    db.session.commit()
    flash('Student deleted successfully')
    return redirect(url_for('students'))

@app.route('/attendance', methods=['GET', 'POST'])
@login_required
def attendance():
    if current_user.role not in ['admin', 'teacher']:
        return redirect(url_for('dashboard'))
    students = get_students_in_alphabetical_order().all()
    if request.method == 'POST':
        date_str = request.form['date']
        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        for student in students:
            status = request.form.get(f'status_{student.id}')
            if not status:
                continue

            existing_attendance = Attendance.query.filter_by(student_id=student.id, date=date).first()
            if existing_attendance:
                existing_attendance.status = status
            else:
                db.session.add(Attendance(student_id=student.id, date=date, status=status))

        db.session.commit()
        flash('Attendance marked successfully for all students')

    return render_template('attendance.html', students=students)

@app.route('/marks', methods=['GET', 'POST'])
@login_required
def marks():
    if current_user.role not in ['admin', 'teacher']:
        return redirect(url_for('dashboard'))
    students = get_students_in_alphabetical_order().all()

    if request.method == 'POST':
        for student in students:
            for subject_key, subject_name in SUBJECTS:
                marks_value = request.form.get(f'marks_{student.id}_{subject_key}', '').strip()
                if not marks_value:
                    continue

                existing_mark = Mark.query.filter_by(student_id=student.id, subject=subject_name).first()
                if existing_mark:
                    existing_mark.marks = float(marks_value)
                else:
                    db.session.add(
                        Mark(student_id=student.id, subject=subject_name, marks=float(marks_value))
                    )

        db.session.commit()
        flash('Marks updated successfully for all students')

    return render_template(
        'marks.html',
        students=students,
        subjects=SUBJECTS,
        student_marks=build_marks_lookup(students)
    )

@app.route('/reports')
@login_required
def reports():
    if current_user.role == 'student':
        student = Student.query.filter_by(user_id=current_user.id).first()
        students = [student] if student else []
    else:
        students = get_students_in_alphabetical_order().all()
    reports = []
    for student in students:
        attendance_count = Attendance.query.filter_by(student_id=student.id, status='Present').count()
        total_attendance = Attendance.query.filter_by(student_id=student.id).count()
        attendance_percentage = (attendance_count / total_attendance * 100) if total_attendance > 0 else 0
        total_marks = sum([m.marks for m in student.marks])
        num_subjects = len(student.marks)
        percentage = (total_marks / (num_subjects * 100) * 100) if num_subjects > 0 else 0
        grade = 'A' if percentage >= 90 else 'B' if percentage >= 80 else 'C' if percentage >= 70 else 'D' if percentage >= 60 else 'F'
        reports.append({
            'student': student,
            'attendance_count': attendance_count,
            'attendance_percentage': attendance_percentage,
            'total_marks': total_marks,
            'percentage': percentage,
            'grade': grade,
            'marks': student.marks
        })
    return render_template('report.html', reports=reports)

@app.route('/export/<int:student_id>')
@login_required
def export(student_id):
    from utils.pdf_generator import generate_pdf
    student = Student.query.get_or_404(student_id)
    if current_user.role == 'student' and student.user_id != current_user.id:
        return redirect(url_for('dashboard'))
    pdf_path = generate_pdf(student)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', password=generate_password_hash('admin'), role='admin')
            db.session.add(admin)
            db.session.commit()
        
        # Add sample students if none exist
        if not Student.query.first():
            sample_students = [
                {"name": "Aarav Sharma", "roll_no": "001", "class_": "10A", "email": "aarav.sharma@school.com", "phone": "9876543210"},
                {"name": "Vihaan Gupta", "roll_no": "002", "class_": "10A", "email": "vihaan.gupta@school.com", "phone": "9876543211"},
                {"name": "Arjun Verma", "roll_no": "003", "class_": "10A", "email": "arjun.verma@school.com", "phone": "9876543212"},
                {"name": "Reyansh Singh", "roll_no": "004", "class_": "10B", "email": "reyansh.singh@school.com", "phone": "9876543213"},
                {"name": "Ishaan Patel", "roll_no": "005", "class_": "10B", "email": "ishaan.patel@school.com", "phone": "9876543214"},
                {"name": "Kabir Joshi", "roll_no": "006", "class_": "10B", "email": "kabir.joshi@school.com", "phone": "9876543215"},
                {"name": "Anaya Kumar", "roll_no": "007", "class_": "10C", "email": "anaya.kumar@school.com", "phone": "9876543216"},
                {"name": "Diya Rao", "roll_no": "008", "class_": "10C", "email": "diya.rao@school.com", "phone": "9876543217"},
                {"name": "Saanvi Nair", "roll_no": "009", "class_": "10C", "email": "saanvi.nair@school.com", "phone": "9876543218"},
                {"name": "Myra Iyer", "roll_no": "010", "class_": "10D", "email": "myra.iyer@school.com", "phone": "9876543219"},
                {"name": "Pari Mehta", "roll_no": "011", "class_": "10D", "email": "pari.mehta@school.com", "phone": "9876543220"},
                {"name": "Zara Khan", "roll_no": "012", "class_": "10D", "email": "zara.khan@school.com", "phone": "9876543221"},
                {"name": "Advait Desai", "roll_no": "013", "class_": "11A", "email": "advait.desai@school.com", "phone": "9876543222"},
                {"name": "Rudra Choudhury", "roll_no": "014", "class_": "11A", "email": "rudra.choudhury@school.com", "phone": "9876543223"},
                {"name": "Vivaan Bansal", "roll_no": "015", "class_": "11A", "email": "vivaan.bansal@school.com", "phone": "9876543224"},
                {"name": "Aryan Saxena", "roll_no": "016", "class_": "11B", "email": "aryan.saxena@school.com", "phone": "9876543225"},
                {"name": "Krishna Malhotra", "roll_no": "017", "class_": "11B", "email": "krishna.malhotra@school.com", "phone": "9876543226"},
                {"name": "Atharv Agarwal", "roll_no": "018", "class_": "11B", "email": "atharv.agarwal@school.com", "phone": "9876543227"},
                {"name": "Shaan Roy", "roll_no": "019", "class_": "12A", "email": "shaan.roy@school.com", "phone": "9876543228"},
                {"name": "Devansh Kapoor", "roll_no": "020", "class_": "12A", "email": "devansh.kapoor@school.com", "phone": "9876543229"}
            ]
            for student_data in sample_students:
                student = Student(**student_data)
                db.session.add(student)
            db.session.flush()

        recalculate_student_roll_numbers()
        db.session.commit()
    app.run(debug=True)
