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

try:
    interval_minutes = int(os.environ['POLLING_INTERVAL_MINUTES'])
except Exception as e:
    print(e)
    interval_minutes = 1

polling_manager = PollingManager(db)
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=interval_minutes)
def timed_job():
    print(f'Polling is run every {interval_minutes} minute/s.')
    polling_manager.poll()

sched.start()

