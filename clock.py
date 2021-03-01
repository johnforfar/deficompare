import os

from apscheduler.schedulers.blocking import BlockingScheduler
from database import SQLLiteDatabase
from polling_manager import PollingManager
from postgres_database import PostgresDatabase


sched = BlockingScheduler()

try:
    use_postgres = os.environ['USE_POSTGRES']
    if bool(use_postgres):
        db = PostgresDatabase()
    else:
        db = SQLLiteDatabase()
except Exception as e:
    db = SQLLiteDatabase()
    print(e)

polling_manager = PollingManager(db)

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('Polling is run every three minutes.')
    polling_manager.poll()

sched.start()

