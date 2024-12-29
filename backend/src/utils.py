import soccerdata as sd
from ...scraper.config import *
from pathlib import Path
# Define the data path as a global variable
DATA_PATH = Path(DATA_PATH)

def data_dir_exists(path: Path, scraper: str) -> None:
    scraper_path = path / scraper
    if not scraper_path.exists():
        scraper_path.mkdir(parents=True, exist_ok=True)

def get_fbref(leagues: list[str]=['ENG-Premier League'], seasons: list[str] = ['2425']) -> sd.FBref:
    """
    Returns fbref scraper instance
    """
    # Create scraper class instance filtering on specific leagues and seasons
    return sd.FBref(leagues=leagues, seasons=seasons, data_dir=DATA_PATH / "fbref", no_store=NO_STORE_DATA, no_cache=NO_CACHE_DATA)

def get_fotmob(leagues: list[str]=['ENG-Premier League'], seasons: list[str] = ['2425']) -> sd.FotMob:
    """
    Returns fotmob scraper instance
    """
    # Create scraper class instance filtering on specific leagues and seasons
    return sd.FotMob(leagues=leagues, seasons=seasons, data_dir=DATA_PATH / "fotmob", no_store=NO_STORE_DATA, no_cache=NO_CACHE_DATA)

def get_understat(leagues: list[str]=['ENG-Premier League'], seasons: list[str] = ['2425']) -> sd.Understat:
    """
    Returns understat scraper instance
    """
    # Create scraper class instance filtering on specific leagues and seasons
    return sd.Understat(leagues=leagues, seasons=seasons, data_dir=DATA_PATH / "understat", no_store=NO_STORE_DATA, no_cache=NO_CACHE_DATA)

def get_whoscored(leagues: list[str]=['ENG-Premier League'], seasons: list[str] = ['2425']) -> sd.WhoScored:
    """
    Returns whoscored scraper instance
    """
    # Create scraper class instance filtering on specific leagues and seasons
    return sd.WhoScored(leagues=leagues, seasons=seasons, data_dir=DATA_PATH / "whoscored", no_store=NO_STORE_DATA, no_cache=NO_CACHE_DATA)