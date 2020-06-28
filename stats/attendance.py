# Import Stuff, steps 1-3
import pandas as pd
import matplotlib.pyplot as plt
import games from data.py

# Select appropriate columns from games DataFrame
attendance = [[ games.loc[games['type'] == 'info',
                games['multi2'] == 'attendance' ],
              [ 'year', 'multi3' ] ]
