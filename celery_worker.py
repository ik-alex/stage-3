# celery_worker.py

from email_tasks import app

if __name__ == '__main__':
    app.start()
