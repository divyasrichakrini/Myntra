import schedule
import time
from daily_update import add_daily_question

# Schedule the add_daily_question function to run every day at a specified time
schedule.every().day.at("00:00").do(add_daily_question)  # Change "00:00" to the desired time

print("Scheduled daily updates. Press Ctrl+C to exit.")

while True:
    schedule.run_pending()
    time.sleep(1)
