"""Quesno-4.

Running the script every one hour.
"""
import time
import schedule


def funcname():
    """Sample function to execute every one hour."""
    print('A simple function!')


def scheduling():
    """Scheduling the func to run every one hour."""
    schedule.every(1).hours.do(funcname)
    while True:
        schedule.run_pending()
        time.sleep(0)


scheduling()
