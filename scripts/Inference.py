from joblib import load
from Ranges import get_ranges
import pandas as pd
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

model_num = 1
model = load(f'../models/model_{model_num}.joblib')

df = pd.read_csv('../data/Verlander_Data/verlander_rowsCLEANED1.csv')
#--------------------------------
plate_x_range, plate_z_range, release_speed_range, release_pos_x_range, release_pos_z_range, release_extension_range, release_spin_rate_range, spin_axis_range = get_ranges()

pitch_names_range = ['Curveball', '4-Seam Fastball', 'Slider', 'Changeup', 'Cutter', '2-Seam Fastball']
stand_range = ['R','L']
#-------------------------------
# pitch_name,release_speed,release_pos_x,release_pos_z,release_extension,release_spin_rate,spin_axis,plate_x,plate_z,stand,description
ranges = [pitch_names_range, release_speed_range, release_pos_x_range, release_pos_z_range, release_extension_range, release_spin_rate_range, spin_axis_range, plate_x_range, plate_z_range,stand_range]
names = ['pitch_name', 'release_speed', 'release_pos_x', 'release_pos_z', 'release_extension', 'release_spin_rate', 'spin_axis', 'plate_x', 'plate_z', 'stand']
user_inputs = []
for range in ranges:
    if range == pitch_names_range:
        while True:
            pitch_name = input(f'Enter a name for pitch_name. Here are the options: {pitch_names_range}: ')
            if pitch_name in pitch_names_range:
                user_inputs.append(pitch_name)
                break
            else:
                print("Invalid pitch name. Please try again.")

    elif range == stand_range:
        while True:
            stand = input(f'Enter a stance for the batter. Your choices are: {range}: ')
            if stand in stand_range:
                user_inputs.append(stand)
                break
            else:
                print("Invalid stance. Please try again.")
    else:
        while True:
            try:
                value = float(input(f'Enter a number for {names[ranges.index(range)]} in the range {range}: '))
                if range[0] <= value <= range[1]:
                    user_inputs.append(value)
                    break
                else:
                    print(f"Value out of range. Please enter a number between {range[0]} and {range[1]}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

user_dict = {name: [user_input] for name, user_input in zip(names, user_inputs)}

user_dataframe = pd.DataFrame(user_dict)

# Fit and transform pitch_name
le.fit(pitch_names_range)
user_dataframe['pitch_name'] = le.transform(user_dataframe['pitch_name'])

# Fit and transform stand
le.fit(stand_range)
user_dataframe['stand'] = le.transform(user_dataframe['stand'])

prediction = model.predict(user_dataframe)
le_description = LabelEncoder()

le_description.fit(df['description'])

decoded_prediction = le_description.inverse_transform(prediction)
print(f"\n\n\nPREDICTION: {decoded_prediction}")

#PROBABILITIES---------------------------------------------
print("Probabilities (in %): \n")
prediction_probability = model.predict_proba(user_dataframe)

class_labels = le_description.classes_
for class_label, prob in zip(class_labels, prediction_probability[0]):
    print(f"{class_label}: {100*prob:.3f}")
 