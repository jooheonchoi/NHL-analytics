import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import TopDownHockey_Scraper.TopDownHockey_EliteProspects_Scraper as tdhepscrape

leagues = "nhl"
seasons = ["2019-2020", "2020-2021"]

nhl_skaters = tdhepscrape.get_skaters(leagues, seasons)
canucks_skaters = nhl_skaters.loc[nhl_skaters.team == "Vancouver Canucks"]
print(canucks_skaters)
