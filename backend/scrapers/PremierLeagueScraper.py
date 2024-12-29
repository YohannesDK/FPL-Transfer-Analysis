from typing import List
from .scraper import Scraper


import soccerdata as sd


class PremierLeagueScraper(Scraper):
  def __init__(self, leagues: List[str] = ['ENG-Premier League'], seasons: List[str] = ['2425'], data_dir_folder: str = 'understat'):
    # Call the base class __init__
    super().__init__(leagues=leagues, seasons=seasons, data_dir_folder=data_dir_folder)

  def initialize_scraper(self, leagues: List[str], seasons: List[str]):
    # Initialize the scraper and return it
    return sd.Understat(
      leagues=leagues,
      seasons=seasons,
      data_dir=self.data_dir,
      no_store=self.no_store,
      no_cache=self.no_cache
    )

  def scrape(self):
    # Implement the specific scraping logic
    return self.scraper.read_player_match_stats()

