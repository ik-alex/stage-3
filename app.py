# app.py

from flask import Flask, request  # type: ignore
from email_tasks import send_email, log_message
import logging
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    sendmail = request.args.get('sendmail')
    talktome = request.args.get('talktome')

    if sendmail:
        send_email.delay(sendmail)
        return f'Email to {sendmail} has been queued.'

    if talktome:
        # log_message.delay()
        # now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # logging.info(f"Current time logged: {now}")
        # return "Logged the current time."
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('/var/log/messaging_system.log', 'a') as f:
            f.write(f'{current_time}: {talktome}\n')
            logging.info(f"Current time logged: {current_time}")
        return f'Current time logged: {current_time}'

    return 'Please provide a valid query parameter.'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
