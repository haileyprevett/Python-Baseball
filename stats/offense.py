import pandas as pd
import matplotlib.pyplot as plt
from data import games

# Get the games of type play and rename columns
plays = games[games['type'] == 'play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

# Select the rows where the event column's value starts with S (not SB), D, T, and HR
# Keep only inning and event cols and assign to new var hits
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'),['inning', 'event']]

# Convert inning col to numeric
hits.loc[:,'inning'] = pd.to_numeric(hits.loc[:,'inning'])

# Create a dictionary
replacements = {
    r'^S(.*)': 'single',
    r'^D(.*)': 'double',
    r'^T(.*)': 'triple',
    r'^HR(.*)': 'hr'
}

# Replace info from events with appropriate values from our dictionary
hit_type = hits['event'].replace(replacements,  regex=True)

# Add new col hit_type to DataFrame hits
hits = hits.assign(hit_type=hit_type)

# Group by inning and hit type
hits = hits.groupby(['inning','hit_type']).size().reset_index(name='count')

# Convert hit type col to categorical
hits.loc[:,'hit_type'] = pd.Categorical(hits.loc[:,'hit_type'],['single', 'double', 'triple', and 'hr'])
