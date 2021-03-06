# Import Stuff, steps 1-3
import pandas as pd
import matplotlib.pyplot as plt
from data import games

# Select appropriate columns from games DataFrame
attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'),
                      ['year', 'multi3']]

# Change col names in DataFrame
attendance.columns = ['year','attendance']

# Convert attendance col to numeric
attendance.loc[:,'attendance'] = pd.to_numeric(attendance.loc[:,'attendance'])

# Plot year v. attendance with a horizontal line to represent the mean
attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')
plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(y=attendance['attendance'].mean(), label='Mean', linestyle='--', color='green')
plt.show()
