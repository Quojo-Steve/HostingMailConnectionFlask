from flask import Flask, render_template,request
from dotenv import load_dotenv
import sqlite3
import os
from flask_mail import Mail, Message

load_dotenv()

app = Flask(__name__)
app.config['MAIL_SERVER']=str(os.getenv('MAIL_SERVER'))
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USERNAME'] = str(os.getenv('MAIL_USERNAME'))
app.config['MAIL_PASSWORD'] = str(os.getenv('MAIL_PASSWORD'))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

def connect_to_db() -> sqlite3.Connection:
    conn = sqlite3.connect('sqlitedb.db')
    return conn

@app.route('/')
def index():
    return 'Hello boys!!!'


@app.route('/db')
def whereami():
    # try:
    #     con = connect_to_db()
    #     con.execute('''
    #         CREATE TABLE users(
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             firstname TEXT NOT NULL,
    #             lastname TEXT NOT NULL,
    #             email TEXT UNIQUE NOT NULL
    #         );
    #     ''')
    #     con.commit()
    #     con.close()
        
    #     return "Sucess"
    # except sqlite3.Error as e:
    #     return str(e)
    return "Ghana"

@app.get("/signup")
@app.post("/signup")
def signup():
    if request.method == "POST":
        firstname = request.form['fname']
        lastname = request.form['lname']
        email = request.form['email']

        try:
            con = connect_to_db()
            con.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id INT PRIMARY KEY AUTOINCREMENT,
                    firstname TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                );
            ''')
            con.execute('''
            INSERT INTO users(
                    firstname,lastname,email
                ) VALUES (?,?,?)
            ''',(firstname,lastname,email))
            con.commit()
            con.close()
            return str("Sucess")
        except sqlite3.Error as e:
            return str(e)
    return render_template('signup.html')

@app.post('/mail')
@app.get('/mail')
def send_mail():
    if request.method == 'POST':
        name = request.form.get('fullName')
        email = request.form.get('email')
        message_sent = request.form.get('message')
        message = Message(
            subject=f"How are you doing today? {name}",
            recipients=["ahmedashafa12@gmail.com"],
            sender=email
        )
        message.body = message_sent
        
        try:
            mail.send(message)
            return render_template('thanks.html')
        except Exception as e:
            return e
    return render_template('form.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)