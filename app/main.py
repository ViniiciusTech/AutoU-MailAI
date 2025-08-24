from flask import Flask, render_template, request
import sqlite3
from datetime import datetime
import os
from classifier import EmailClassifier
from responder import ResponseGenerator
from utils import process_file, get_stats, save_email_result  

app = Flask(__name__)

# CFG dados
DATABASE = 'data/emails.db'

def init_db():
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            category TEXT NOT NULL,
            confidence REAL NOT NULL,
            sentiment TEXT NOT NULL,
            keywords TEXT NOT NULL,
            suggested_response TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_email_history(limit=10):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM emails 
        ORDER BY created_at DESC 
        LIMIT ?
    ''', (limit,))
    emails = cursor.fetchall()
    conn.close()

    result = []
    for email in emails:
        email_dict = dict(email)
        email_dict['created_at'] = datetime.fromisoformat(email_dict['created_at'])
        result.append(email_dict)
    
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        email_content = ""

        if request.form.get('email_text'):
            email_content = request.form.get('email_text')

        elif 'email_file' in request.files:
            file = request.files['email_file']
            if file.filename:
                email_content = process_file(file)

        if email_content:
            classifier = EmailClassifier()
            classification = classifier.classify(email_content)

            responder = ResponseGenerator()
            response = responder.generate_responses(email_content, classification)

            result = {
                'category': classification['category'],
                'confidence': classification['confidence'],
                'sentiment': classification['sentiment'],
                'keywords': classification['keywords'],
                'suggested_response': response
            }

            save_email_result(email_content, result)

    stats = get_stats(DATABASE)
    history = get_email_history()
    return render_template('index.html', result=result, stats=stats, history=history)

# Inicialização do app
if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
