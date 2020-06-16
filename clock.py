from datetime import datetime
from lovebird import sendLove
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(sendLove, 'interval', seconds=10)

sched.start()
