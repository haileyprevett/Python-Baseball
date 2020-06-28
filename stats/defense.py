import pandas as pd
import matplotlib.pyplot as plt
from frames import games
from frames import info
from frames import events

# Keep games where type is play and event is not NP
plays = games.query("type=='play' & event!='NP'")
# Rename columns
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

# Remove rows for same consecutive at bat
pa = plays.loc[plays['player'].shift() != plays['player'], ['year', 'game_id', 'inning', 'team', 'player']]
# Group plate appearances
pa = pa.groupby(['year','game_id','team']).size().reset_index(name='PA')

# Set the index of the events DataFrame
events = events.set_index(['year','game_id','team','event_type'])
# Unstack the DataFrame
events = events.unstack().fillna(0).reset_index()
# Manage column labels
events.columns = events.columns.droplevel()
events.columns = ['year', 'game_id', 'team', 'BB', 'E', 'H', 'HBP', 'HR', 'ROE', 'SO']
events = events.rename_axis(None, axis='columns')

# Merge pa and events DataFrames
events_plus_pa = pd.merge(events,pa,how='outer',left_on=['year','game_id','team'],right_on=['year','game_id','team'])
# Merge again with info
defense = pd.merge(events_plus_pa,info)

# Calculate the DER
defense.loc[:, 'DER'] = 1 - ((defense['H'] + defense['ROE']) / (defense['PA'] - defense['BB'] - defense['SO'] - defense['HBP'] - defense['HR']))
#       HBP = Hit-by-pitch OR Hailey Brooke Prevett :)
# Convert year col to numeric
defense.loc[:,'year'] = pd.to_numeric(defense.loc[:,'year'])

# reshape with pivot
der = defense.loc[defense['year']>=1978, ['year','defense','DER']]
der = der.pivot(index='year',columns='defense', values='DER')

# Plot
der.plot(x_compat=True,xticks=range(1978,2018,4), rot=45)
plt.show()
