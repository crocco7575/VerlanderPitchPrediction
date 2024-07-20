import pandas as pd


df = pd.read_csv('../data/Verlander_Data/verlander_rowsCLEANED.csv')


numeric_columns = ['release_speed', 'release_pos_x', 'release_pos_z', 'release_extension', 'release_spin_rate', 'spin_axis', 'plate_x', 'plate_z']

# Clean the numeric columns by converting non-numeric values to NaN
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

df = df.dropna()

''' Save the cleaned data to a new CSV file '''

df.to_csv('../data/Verlander_Data/verlander_rowsCLEANED1.csv', index=False)