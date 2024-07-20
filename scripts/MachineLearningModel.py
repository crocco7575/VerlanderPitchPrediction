import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump

df = pd.read_csv('../data/Verlander_Data/verlander_rowsCLEANED1.csv')


# -----------------------------
model_num = 1
n_estimators = 500
random_state = 10
# -----------------------------


# Cleaning dataset
le = LabelEncoder()
df['pitch_name'] = le.fit_transform(df['pitch_name'])
df['stand'] = le.fit_transform(df['stand'])
df['description'] = le.fit_transform(df['description'])

# Split data: train/test
X = df.drop('description', axis=1)

y = df['description']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=random_state)

# Training
model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
model.fit(X_train, y_train)
print("Done with training!")

#Saving model
dump(model, f'../models/model_{model_num}.joblib')


# Eval
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=1))

