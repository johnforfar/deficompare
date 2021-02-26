import time

from constants import POLLING_DELAY_SECONDS
from database import SQLLiteDatabase

from polling_manager import PollingManager


# For now just a temp starting point for the backend testing

import multiprocessing


def worker():
    """worker thread for running the polling and database updates"""
    db = SQLLiteDatabase()
    polling_manager = PollingManager(db)
    while True:
        # Main loop for polling APIs
        polling_manager.poll()
        time.sleep(POLLING_DELAY_SECONDS)


def main():
    p = multiprocessing.Process(target=worker, args=())
    p.start()


if __name__ == '__main__':
    main()

