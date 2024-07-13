# email_tasks.py

from celery import Celery 
import logging
from datetime import datetime
from config import broker_url, result_backend, smtp_server, smtp_port, smtp_username, smtp_password
import smtplib
from email.mime.text import MIMEText

app = Celery('email_tasks', broker=broker_url, backend=result_backend)

@app.task
def send_email(to_email):
    msg = MIMEText('Welcome to HNG Devops. We are currently in stage 3.')
    msg['Subject'] = 'HNG Email'
    msg['From'] = smtp_username
    msg['To'] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, [to_email], msg.as_string())

@app.task
def log_message():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"Current time logged: {now}")
    print("Message logged")
