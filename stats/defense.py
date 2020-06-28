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
