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
# Reset index
strike_outs = strike_outs.reset_index(name='strike_outs')
# Convert number of strike outs to numeric
strike_outs = strike_outs.loc[:,['year', 'strike_outs']].apply(pd.to_numeric)

strike_outs.plot(x='year', y='strike_outs', kind='scatter').legend(['Strike outs'])
plt.show()
