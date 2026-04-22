from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
import os

def generate_pdf(student):
    filename = f"{student.name.replace(' ', '_')}_marksheet.pdf"
    filepath = os.path.join(os.getcwd(), filename)
    doc = SimpleDocTemplate(filepath, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph("Student Marksheet", styles['Title']))
    story.append(Spacer(1, 12))

    # Student Details
    story.append(Paragraph(f"Name: {student.name}", styles['Normal']))
    story.append(Paragraph(f"Roll Number: {student.roll_no}", styles['Normal']))
    story.append(Paragraph(f"Class: {student.class_}", styles['Normal']))
    story.append(Paragraph(f"Email: {student.email}", styles['Normal']))
    story.append(Paragraph(f"Phone: {student.phone}", styles['Normal']))
    story.append(Spacer(1, 12))

    # Marks Table
    data = [['Subject', 'Marks']]
    total_marks = 0
    for mark in student.marks:
        data.append([mark.subject, str(mark.marks)])
        total_marks += mark.marks
    data.append(['Total', str(total_marks)])
    percentage = (total_marks / (len(student.marks) * 100) * 100) if student.marks else 0
    grade = 'A' if percentage >= 90 else 'B' if percentage >= 80 else 'C' if percentage >= 70 else 'D' if percentage >= 60 else 'F'
    data.append(['Percentage', f"{percentage:.2f}%"])
    data.append(['Grade', grade])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    story.append(table)

    doc.build(story)
    return filepath