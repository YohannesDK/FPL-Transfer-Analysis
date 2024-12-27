import soccerdata as sd


def get_shooting_data():
    """
    Fetch basic Premier League data using SoccerData.
    """

    # Create scraper class instance filtering on specific leagues and seasons
    fbref = sd.FBref(leagues=['ENG-Premier League'], seasons=['2425'])
    # Retrieve data for the specified leagues and seasons
    return fbref.read_team_season_stats(stat_type='shooting')
