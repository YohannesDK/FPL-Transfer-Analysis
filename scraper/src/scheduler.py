from jobs.test_job import test_scraper_job
from apscheduler.schedulers.blocking import BlockingScheduler
from config import DATA_PATH
from logger import setup_logger

# Configure logger
logger = setup_logger('scheduler')

def main():
    scheduler = BlockingScheduler()

    # Schedule a job to run every 5 minutes
    scheduler.add_job(test_scraper_job, "interval", minutes=1)

    logger.info("Scheduler started. Press Ctrl+C to exit.")
    # print("Scheduler started. Press Ctrl+C to exit.")
    print(f"Data path: {DATA_PATH}")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        # print("Scheduler stopped.")
        logger.info("Scheduler stopped.")

if __name__ == "__main__":
    main()

