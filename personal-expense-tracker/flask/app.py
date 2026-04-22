from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

EXPENSES_FILE = 'expenses.json'

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r') as f:
            return json.load(f)
    return {"expenses": []}

def save_expenses(data):
    with open(EXPENSES_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/expenses', methods=['GET'])
def get_expenses():
    data = load_expenses()
    current_month = datetime.now().strftime('%Y-%m')
    monthly_expenses = [exp for exp in data['expenses'] if exp['date'].startswith(current_month)]
    # Calculate totals
    categories = ['Food', 'Transport', 'Shopping', 'Other']
    totals = {cat: 0 for cat in categories}
    grand_total = 0
    for exp in monthly_expenses:
        if exp['category'] in totals:
            totals[exp['category']] += exp['amount']
        grand_total += exp['amount']
    data['expenses'] = monthly_expenses  # show only monthly
    data['totals'] = totals
    data['grand_total'] = grand_total
    return jsonify(data)

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = load_expenses()
    new_exp = request.json
    new_exp['id'] = max([e.get('id', 0) for e in data['expenses']] + [0]) + 1
    new_exp['date'] = datetime.now().strftime('%Y-%m-%d')
    data['expenses'].append(new_exp)
    save_expenses(data)
    return jsonify({"message": "Added"})

@app.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    data = load_expenses()
    data['expenses'] = [e for e in data['expenses'] if e['id'] != id]
    save_expenses(data)
    return jsonify({"message": "Deleted"})

if __name__ == '__main__':
    app.run(debug=True)