import pandas as pd

df = pd.read_csv('../data/Verlander_Data/verlander_rowsCLEANED.csv')
# Convert 'plate_x' and 'plate_z' to numeric values

def get_ranges(df=pd.read_csv('../data/Verlander_Data/verlander_rowsCLEANED.csv')):
    df['plate_x'] = pd.to_numeric(df['plate_x'], errors='coerce')
    df['plate_z'] = pd.to_numeric(df['plate_z'], errors='coerce')
    df['release_speed'] = pd.to_numeric(df['release_speed'], errors='coerce')
    df['release_pos_x'] = pd.to_numeric(df['release_pos_x'], errors='coerce')
    df['release_pos_z'] = pd.to_numeric(df['release_pos_z'], errors='coerce')
    df['release_extension'] = pd.to_numeric(df['release_extension'], errors='coerce')
    df['release_spin_rate'] = pd.to_numeric(df['release_spin_rate'], errors='coerce')

    # 'release_speed', 'release_pos_x', 'release_pos_z', 'release_extension', 'release_spin_rate'
    # Drop any rows with non-numeric values
    df = df.dropna(subset=['plate_x', 'plate_z', 'release_speed', 'release_pos_x', 'release_pos_z', 'release_extension', 'release_spin_rate'])

    plate_x_range = (float(df['plate_x'].min()), float(df['plate_x'].max()))
    plate_z_range = (float(df['plate_z'].min()), float(df['plate_z'].max()))
    release_speed_range = (float(df['release_speed'].min()), float(df['release_speed'].max()))
    release_pos_x_range = (float(df['release_pos_x'].min()), float(df['release_pos_x'].max()))
    release_pos_z_range = (float(df['release_pos_z'].min()), float(df['release_pos_z'].max()))
    release_extension_range = (float(df['release_extension'].min()), float(df['release_extension'].max()))
    release_spin_rate_range = (float(df['release_spin_rate'].min()), float(df['release_spin_rate'].max()))
    spin_axis_range = (float(df['spin_axis'].min()), float(df['spin_axis'].max()))
    # print("Plate X Range:", plate_x_range)
    # print("Plate Z Range:", plate_z_range)
    # print("release speed Range:", release_speed_range)
    # print("release pos_x Range:", release_pos_x_range)
    # print("release pos_z Range:", release_pos_z_range)
    # print("release extension Range:", release_extension_range)
    # print("release spin rate Range:", release_spin_rate_range)

    return plate_x_range, plate_z_range, release_speed_range, release_pos_x_range, release_pos_z_range, release_extension_range, release_spin_rate_range, spin_axis_range

get_ranges(df=df)