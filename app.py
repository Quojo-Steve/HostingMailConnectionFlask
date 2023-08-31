from flask import Flask, render_template
from dotenv import load_dotenv
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

@app.route('/')
def index():
    return 'Hello boys!!!'


@app.route('/whereami')
def whereami():
    return "Ghana"

@app.post('/mail')
def send_mail():
    message = Message(
        subject="How are you doing today?",
        recipients=["ahmedashafa12@gmail.com"],
        sender="quojosteve@gmail.com"
    )
    message.body = "I sent you a message mf "
    
    try:
        mail.send(message)
        return "Sucessful"
    except Exception as e:
        return e

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)