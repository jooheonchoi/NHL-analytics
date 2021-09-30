import requests
import pandas as pd

url = "https://statsapi.web.nhl.com/api/v1/"
team = input("search for a team: ")
r = requests.get(url + "teams/")

data = r.json()
df = pd.json_normalize(data["teams"])

teamdf = df.loc[df.name == team]
teamID = str(teamdf.id.iloc[0])
print(team +"'s id is: " + teamID)



# get schedule
seasons = "20182019"
r = requests.get(url + "schedule?season=" + seasons + "&gameType=R&site=en_nhl&teamId=" + teamID)
data = r.json()
df = pd.DataFrame(data["dates"])








