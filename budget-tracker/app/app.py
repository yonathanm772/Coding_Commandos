from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)
DB_FILE = 'spending.db'

# Initialize Database
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)

@app.route('/')
def index():
    # Get all transactions from the database to display on the homepage
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute("SELECT id, description, amount, date FROM transactions")
        transactions = cursor.fetchall()
    return render_template('index.html', transactions=transactions)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        with sqlite3.connect(DB_FILE) as conn:
            conn.execute("INSERT INTO transactions (description, amount) VALUES (?, ?)",
                         (description, amount))
        return redirect('/')  # Redirect to homepage after adding a transaction
    return render_template('index.html')  # Use index.html for the "add" page too

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
