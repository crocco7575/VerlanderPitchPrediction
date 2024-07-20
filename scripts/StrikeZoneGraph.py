import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Load the updated CSV file
df = pd.read_csv('../data/Verlander_Data/verlander_rowsCLEANED.csv')

# Convert 'plate_x' and 'plate_z' to numeric values
df['plate_x'] = pd.to_numeric(df['plate_x'], errors='coerce')
df['plate_z'] = pd.to_numeric(df['plate_z'], errors='coerce')

# Drop any rows with non-numeric values
df = df.dropna(subset=['plate_x', 'plate_z'])

plt.figure(figsize=(8, 8))

# Plot plate_x and plate_z with different colors for each pitch type
for pitch_type in df['pitch_name'].unique():
    pitch_df = df[df['pitch_name'] == pitch_type]
    plt.scatter(pitch_df['plate_x'], pitch_df['plate_z'], label=pitch_type)

# Define the strike zone boundaries
strike_zone_x = [-0.95, 0.95]
strike_zone_z = [1.2, 3.8]

# Plot the strike zone as a rectangle with a bold and black border
strike_zone = patches.Rectangle((strike_zone_x[0], strike_zone_z[0]), 
                                strike_zone_x[1]-strike_zone_x[0], 
                                strike_zone_z[1]-strike_zone_z[0], 
                                edgecolor='black', facecolor='none', linewidth=10)

plt.gca().add_patch(strike_zone)

# Set the axis limits to the range of plate_x and plate_z
plt.xlim(df['plate_x'].min()-0.1, df['plate_x'].max()+0.1)
plt.ylim(df['plate_z'].min()-0.1, df['plate_z'].max()+0.1)

# Add labels and legend
plt.xlabel('plate_x')
plt.ylabel('plate_z')
plt.title('Strike Zone and Pitch Locations')
plt.legend()

# Show the plot
# plt.show()
plt.savefig('../data/Verlander_Data/StrikeZoneGraph.pdf')