from flask import Flask, render_template,request
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