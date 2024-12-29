from jobs.test_job import test_scraper_job
from apscheduler.schedulers.blocking import BlockingScheduler

def main():
    scheduler = BlockingScheduler()
    
    # Schedule the test_scraper_job every X minutes
    X = 2  # Set interval (in minutes)
    scheduler.add_job(test_scraper_job, "interval", minutes=X, id="test_scraper_job")
    
    print(f"Scheduler started. Job will run every {X} minutes.")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")

if __name__ == "__main__":
    main()
