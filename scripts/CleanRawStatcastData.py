import csv

with open('../data/Raw_Statcast_Data/Statcast_2017.csv', 'r') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    rows = [row for row in reader if row['player_name'] == 'Verlander, Justin']

with open('../data/verlander_rows.csv', 'a', newline='') as new_file:
    writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)