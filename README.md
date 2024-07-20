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
	- This dataset was cleaned [here](/scripts/CleanRawStatcastData.py)

