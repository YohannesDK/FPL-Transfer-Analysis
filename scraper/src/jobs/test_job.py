import os
import json
from datetime import datetime
from scrapers.PremierLeagueScraper import PremierLeagueScraper

def test_scraper_job():
    # Initialize scraper
    scraper = PremierLeagueScraper()
    
    # Fetch sample data (replace with actual scraper method)
    data = scraper.get_fixtures()  # Replace with the actual method in your scraper
    
    # Prepare output directory
    output_dir = "scraper/data/test_data"
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a timestamped JSON file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"test_data_{timestamp}.json")
    
    # Write the data to the file
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"[{datetime.now()}] Data written to {output_file}")
