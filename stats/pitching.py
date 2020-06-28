# Import stuff
import pandas as pd
import matplotlib.pyplot as plt
from data import games

# Grab games of type "play"
plays = games[games['type'] == 'play']

# Select all strike outs
strike_outs = plays[plays['event'].str.contains('K')]

# Group by year and game
strike_outs = strike_outs.groupby(['year', 'game_id']).size()
