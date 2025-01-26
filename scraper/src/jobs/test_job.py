import os
import json
from datetime import datetime
import pandas as pd
from scrapers.PremierLeagueScraper import PremierLeagueScraper
from logger import setup_logger

# Configure logger
logger = setup_logger('test_scraper_job')

def test_scraper_job():
    logger.info("Running test scraper job")

    # Initialize scraper
    scraper = PremierLeagueScraper()
    
    data = scraper.scrape()
    
    # Convert DataFrame to dictionary
    if isinstance(data, pd.DataFrame):
        data = data.to_dict(orient='records')
    
    # Prepare output directory
    output_dir = "scraper/data/test_data"
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a timestamped JSON file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"test_data_{timestamp}.json")
    
    # Write the data to the file
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"Data written to {output_file}")
