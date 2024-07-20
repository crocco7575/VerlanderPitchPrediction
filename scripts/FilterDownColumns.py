import pandas as pd

df = pd.read_csv('../data/Verlander_Data/verlander_rows.csv')

df = df[['pitch_name', 'release_speed', 'release_pos_x', 'release_pos_z', 
         'release_extension', 'release_spin_rate', 'spin_axis',  
         'plate_x', 'plate_z', 'stand', 'description']]

# Save the updated DataFrame to a new CSV file
df.to_csv('../data/Verlander_Data/verlander_rowsCLEANED.csv', index=False)