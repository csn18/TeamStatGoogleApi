import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TeamStatGoogleApi.settings')

app = Celery('TeamStatGoogleApi')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

"""
This setting celery for update user data in database every day in 04:00AM UTC
"""
app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'Users.tasks.get_stats_from_sheets',
        # 'schedule': crontab(hour="4", minute="0")
        'schedule': crontab(minute="*/1")
    },
}
