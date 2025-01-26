from pathlib import Path
from typing import List, Union
from abc import ABC, abstractmethod
from config import *

import soccerdata as sd


class Scraper(ABC):
  def __init__(self, leagues: List[str] = ['ENG-Premier League'], seasons: List[str] = ['2425'], data_dir_folder: str = 'understat'):
    self.leagues = leagues
    self.seasons = seasons
    self.data_dir = Path(DATA_PATH) / data_dir_folder
    self.no_store = NO_STORE_DATA
    self.no_cache = NO_CACHE_DATA

    # Call the abstract method to initialize the scraper and store it
    self.scraper: Union[sd.FBref, sd.Understat] = self.initialize_scraper(leagues, seasons)

  @abstractmethod
  def initialize_scraper(self, leagues: List[str], seasons: List[str]):
    """
    Abstract method to initialize and return a specific scraper. 
    Must be implemented by subclasses.
    """
    pass

  @abstractmethod
  def scrape(self):
    """
    Abstract method for scraping logic. Must be implemented by subclasses.
    """
    pass