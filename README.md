# Justin Verlander Pitch Prediction Project


## Requirements
```
pip install pandas
pip install sci-kit learn
pip install joblib
pip install matplotlib
```
## Overview
- #### Using a trained machine learning model, we are able to predict a Justin Verlander pitch outcome given user-input pitch data


## Data
- #### Justin Verlander data was gathered from 2017-2019 MLB Statcast Datsets
	- Statcast is a state-of-the-art tracking system used in every MLB game to gather pitch, batting, and event data for analysis. It was implemented in 2015 and became available to the public in 2017.
	- Here is the link to the Kaggle download: [[[https://www.kaggle.com/datasets/s903124/mlb-statcast-data](https://www.kaggle.com/datasets/s903124/mlb-statcast-data)]]
	- Each dataset contains 700k + individual pitches from the respective season.
- #### The Justin Verlander dataset used for training contains 10k + individual pitches from the 2017-2019 seasons
	- The big statcast datasets were cleaned for Justin Verlander pitches in [CleanRawStatcastData.py](/scripts/CleanRawStatcastData.py) and a new dataset was created: [verlander_rows.csv](data/Verlander_Data/verlander_rows.csv)
	- [verlander_rows.csv](data/Verlander_Data/verlander_rows.csv) was then cleaned for desired columns (features used in our model) in [FilterDownColumns.py](scripts/FilterDownColumns.py) and stored in [verlander_rowsCLEANED.csv](data/Verlander_Data/verlander_rowsCLEANED.csv) 
			- The decision on which columns to keep/cut was purely my decision. I just chose the stats that are most prominent and which I was most familiar with
			- Columns kept include: pitch_name,release_speed,release_pos_x,release_pos_z,release_extension,release_spin_rate,spin_axis,plate_x,plate_z,stand,description
	- Lastly, the dataset was scanned for non-numeric values in [CleanNumericColumns.py](scripts/CleanNumericColumns.py) and stored in [verlander_rowsCLEANED1.csv](data/Verlander_Data/verlander_rowsCLEANED1.csv) 
	- 'Description' is the column we are trying to predict, and the rest are used in the model as features to help predict the 'description' of a pitch

## Model

- #### The machine learning algorithm implemented is a Random Forest Classifier
	- Decision Trees are created by selecting a batch of random features (columns in this case), and each tree makes a decision based on those features
	- The algorithim then does a majority vote of all the trees to determine a final output
	- For more information visit the [sci-kit learn website for the Random Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- #### Our train/test split is 80% / 20%
	- Played around with 90/10 and 85/15 but found nearly no difference in results
- #### Results
	- Accuracy for ```model_1.joblib``` after training was 50.196%
	- Pasted here is the classification report:
```
	Classification Report:
              precision    recall  f1-score   support

           0       0.66      0.86      0.75       623
           1       0.29      0.06      0.09        36
           2       0.45      0.56      0.50       328
           3       0.39      0.50      0.44       438
           4       1.00      0.00      0.00         5
           5       1.00      0.00      0.00        25
           7       0.34      0.19      0.24       320
           8       0.27      0.09      0.14       243
           9       0.00      0.00      0.00        18

    accuracy                           0.50      2036
   macro avg       0.49      0.25      0.24      2036
weighted avg       0.47      0.50      0.46      2036
```

## Strike Zone Graph
- #### In [StrikeZoneGraph.py](scripts/StrikeZoneGraph.py), a ```matplotlib``` scatter plot graph is created showing every pitch thrown by Verlander from 2017-2019, which are overlayed on a strike zone
	- Each pitch type has a color-code
	- ```plate_x``` and ```plate_z``` are used to graph the coordinates of each pitch
	- The ```matplotlib``` graph can be seen [here](data/Verlander_Data/StrikeZoneGraph)
## Inference

- #### Users are prompted to enter in data for a "inference", or a model's prediction on brand-new data
	- Ranges are gathered from [Ranges.py](scripts/Ranges.py) to display to the user, which guides them on a number/String to enter in for each feature
	- This input data is stored in a dataframe to give to the loaded model for a prediction 
- #### A prediction is made from the loaded model, and decoded with the ```Label_Encoder()``` class from the ```sklearn.preprocessing``` package
- #### Probabilities for each possible description are also displayed on the screen, showing to the user the "behind the scenes thoughts" of the model
	- ```model.predict_proba``` collects the probability for each description
	- We then iterate through each label and display the probability for each outcome in the terminal
	- Here is an example output to the user after they enter in inference data:
```
PREDICTION: ['ball']
Probabilities (in %): 

ball: 66.171
blocked_ball: 0.212
called_strike: 5.205
foul: 8.402
foul_bunt: 0.095
foul_tip: 1.458
hit_by_pitch: 0.672
hit_into_play: 8.813
swinging_strike: 8.950
swinging_strike_blocked: 0.023
```

# END
