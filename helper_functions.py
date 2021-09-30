import requests
import numpy as np
import pandas as pd
import pickle
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
color_map = plt.cm.winter
from matplotlib.patches import RegularPolygon
import math
from PIL import Image

'''
NHL API: https://gitlab.com/dword4/nhlapi/-/tree/master

More info: 

inspirations:
https://towardsdatascience.com/nhl-analytics-with-python-6390c5d3206d
https://towardsdatascience.com/python-hockey-analytics-tutorial-b0883085938a#ee0a
https://github.com/rkipp1210/data-projects/tree/master/hockey-shot-blocking
'''


def get_team_table():
    path = "data/teams.csv"
    try:
        teamdf = pd.read_csv(path, index_col= 0)
    except:
        r = requests.get("https://statsapi.web.nhl.com/api/v1/teams/")
        data = r.json()
        df = pd.json_normalize(data["teams"])
        df.to_csv(path)
    return teamdf


def get_team_id(teamdf, team_name):
    teamid = -1
    try:
        teamid = teamdf.loc[teamdf.name == team_name, "id"].values[0]
        print(teamid)
    except:
        print("something went wrong in get_team_id")
    return teamid

# season: string, format like "20182019 for the 2018-2019 season.
def team_games_by_season(teamid, season):
    r = requests.get(
        "https://statsapi.web.nhl.com/api/v1/" + "schedule?season="
        + season + "&gameType=R&site=en_nhl&teamId=" + '23')
    data = r.json()
    df = pd.DataFrame(data["dates"])
    dates = df.date.tolist()

    gamedf = pd.DataFrame(df.games.tolist())
    gamedf.columns = ['games']

    gamedf = pd.json_normalize(gamedf.games)
    gamedf = gamedf.loc[:, ['gamePk', 'link', 'gameType', 'season', 'status.abstractGameState']]
    gamedf['date'] = dates
    print(gamedf)
    return gamedf


'''
gamedata goes:
{
copyright
gamePk
link
metadata
gameData: {game, datetime, status, teams, players}
**liveData**: 
}

liveData goes: 
{
plays: {}
}'''
def get_game_data(gamedf):
    gamelinks = gamedf.link.tolist()

    data = []
    for gamelink in gamelinks:
        data.append(None)


teamdf = get_team_table()
teamid = get_team_id(teamdf, "New Jersey Devils")
gamedf = team_games_by_season(teamid,"20182019")


