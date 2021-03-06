import requests
import pickle
import pandas as pd

''' from https://towardsdatascience.com/nhl-analytics-with-python-6390c5d3206d '''

# Set up the API call variables
game_data = []
year = '2019'
season_type = '02'
max_game_ID = 4

# Loop over the counter and format the API call
for i in range(0,max_game_ID):
    r = requests.get(url='http://statsapi.web.nhl.com/api/v1/game/'
        + year + season_type +str(i).zfill(4)+'/feed/live')
    data = r.json()
    game_data.append(data)
    print(data)
    print('iteration ' + str(i))


with open('./'+year+'FullDataset.pkl', 'wb') as f:
    pickle.dump(game_data, f, pickle.HIGHEST_PROTOCOL)

with open('./'+year+'FullDataset.pkl', "rb") as f:
    object = pickle.load(f)

df = pd.DataFrame(object)
df.to_csv(r'file.csv')