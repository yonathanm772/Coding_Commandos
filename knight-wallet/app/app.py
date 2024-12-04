from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)
DB_FILE = 'spending.db'

# Initialize Database
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        # Drop the existing table if it exists (this will delete all data!)
        conn.execute("DROP TABLE IF EXISTS transactions")

        # Create the table with the correct schema
        conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            quantity INTEGER NOT NULL DEFAULT 1,
            total REAL NOT NULL,
            date TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)

@app.route('/')
def index():
    # Get all transactions from the database to display on the homepage
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute("SELECT id, description, amount, quantity, total, date FROM transactions")
        transactions = cursor.fetchall()
    return render_template('index.html', transactions=transactions)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        quantity = request.form['quantity']  # Capture quantity
        
        # Calculate total
        total = float(amount) * int(quantity)
        
        # Insert data into the database
        with sqlite3.connect(DB_FILE) as conn:
            conn.execute("""
            INSERT INTO transactions (description, amount, quantity, total)
            VALUES (?, ?, ?, ?)
            """, (description, amount, quantity, total))
        
        # Redirect to the homepage after adding the transaction
        return redirect('/')
    
    return render_template('index.html')  # Use index.html for the "add" page too

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
