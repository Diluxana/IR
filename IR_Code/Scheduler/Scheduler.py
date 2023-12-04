from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler


def Latest():
    print('Checking for any latest data')
    os.system('python crawl -o Crawler/Papers/FCS_ResearchPapers.json')


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(Latest, 'interval', days=7)
    scheduler.start()
