# -*- coding: utf-8 -*-
"""Bank_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/146h6VZhfEBBimfqjDxO-4gizveWASlRf
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn import model_selection

from warnings import filterwarnings
filterwarnings('ignore')

file_path = 'bank.csv'
bank_data = pd.read_csv(file_path)

data = pd.read_csv(file_path, delimiter=';')

df.head()

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Kategorik değişkenleri sayısal hale dönüştürme
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])

# Hedef ve özellik değişkenlerini ayırma
X = data.drop('y', axis=1)
y = data['y']

# Veri setini eğitim ve test seti olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Random Forest sınıflandırıcısını tanımlama
rf = RandomForestClassifier(random_state=42)

# Hiperparametre aralıklarını tanımlama
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# GridSearchCV ile hiperparametre optimizasyonu
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# En iyi parametreleri ve modeli al
best_params = grid_search.best_params_
best_rf = grid_search.best_estimator_

# Test seti üzerinde tahmin yapma
y_pred = best_rf.predict(X_test)

# Modelin performansını değerlendirme
accuracy = accuracy_score(y_test, y_pred)
classification_report = classification_report(y_test, y_pred)

best_params, accuracy, classification_report

from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score

# Training a basic LightGBM model
lgbm = LGBMClassifier(random_state=42)
lgbm.fit(X_train, y_train)

# Predicting on the test set
y_pred = lgbm.predict(X_test)

# Calculating accuracy
accuracy = accuracy_score(y_test, y_pred)
accuracy

from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

# Create an XGBoost classifier
xgb = XGBClassifier(random_state=42)

# Fit the model to the training data
xgb.fit(X_train, y_train)

# Predict on the test set
y_pred_xgb = xgb.predict(X_test)

# Calculate the accuracy
accuracy_xgb = accuracy_score(y_test, y_pred_xgb)

accuracy_xgb