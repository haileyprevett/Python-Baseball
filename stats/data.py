# Import built in libraries
import os
import glob

# Import Pandas
import pandas as pd

# Python file management
game_files = glob.glob(os.path.join(os.getcwd(),'games','*.EVE'))
game_files.sort()

# Sorting file names
game_frames = []

# Read CSV files & append game frames
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names=['type', 'multi2', 'multi3','multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)

# Concanenate game frames
games = pd.concat(game_frames)

# Clean values
games.loc[games['multi5'] == '??', ['multi5']] = ''

# Extract & forward fill identifiers
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
identifiers = identifiers.fillna(method='ffill')

# Rename columns
identifiers.columns = ['game_id', 'year']
