# Runs the job at 8 AM daily except Fri/Sat
import schedule
import time
import datetime
import os

def job():
    print("Running script...")  
    # 👉 replace with your actual function or script logic
    # os.system("python core/emailer.py")  # if you want to run another script

# Schedule job every day at 08:00
schedule.every().day.at("08:00").do(job)

while True:
    now = datetime.datetime.now()
    print(now)
    print(now.weekday())
    # Skip Friday (4) and Saturday (5)  [Python: Monday=0, Sunday=6]
    if now.weekday() not in (4, 5):
        schedule.run_pending()
    time.sleep(30)
