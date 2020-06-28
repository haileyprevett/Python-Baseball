import pandas as pd
import matplotlib.pyplot as plt
from data import games

# Get the games of type play and rename columns
plays = games[games['type'] == 'play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

# Select the rows where the event column's value starts with S (not SB), D, T, and HR
plays = plays[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)')]
# Keep only inning and event cols and assign to new var hits
hits = plays[:,['inning', 'event']]

# strike_outs = strike_outs.loc[:,['year', 'strike_outs']].apply(pd.to_numeric)

hits = hits.loc[:,['inning']].apply(pd.to_numeric)
