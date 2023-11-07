from os import PathLike
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump
import pandas as pd
import pathlib

df = pd.read_csv(pathlib.Path('data/machine-failure.csv'))
y = df.pop('Torque')
X = df
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)

print ('Training model.. ')
clf = RandomForestClassifier(n_estimators = 20,
                            max_depth=100,
                            random_state=0)
clf.fit(X_train, y_train)
print ('Saving model..')

dump(clf, pathlib.Path('model/machine-failure.csv-v1.joblib'))
