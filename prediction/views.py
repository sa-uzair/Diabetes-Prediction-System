from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from . import views
def Home(request):
    return render(request,'prediction/Home.html')
def prediction(request):
    return render(request,'prediction/page1.html')
def result(request):
    dataset = pd.read_csv(r'C:\Users\Sania\diabetes.csv')
    le = LabelEncoder()
    dataset["Gender"] = le.fit_transform(dataset["Gender"])
    Gender = pd.DataFrame({'Gender': ['Male', 'Female']})
    feature_columns = ['Gender', 'Fasting', 'After_Meal', 'Pre_Meal', 'A1c', 'BMI', 'Age']
    X = dataset[feature_columns].values
    y = dataset['Outcome']
    models = []
    models.append(('RF', RandomForestClassifier()))
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=dataset.Outcome, test_size=0.33,random_state=0)
    names = []
    scores = []
    for name, model in models:
        model.fit(X_train, y_train)

        if 'n0' == 'Female':
            val0=0
        else:
            val0=1
        val1 = float(request.GET['n4'])
        val2 = float(request.GET['n6'])
        val3 = float(request.GET['n5'])
        val4 = float(request.GET['n2'])
        val5 = float(request.GET['n1'])
        val6 = float(request.GET['n3'])
        pred = model.predict([[val0,val1,val2,val3,val4,val5,val6]])
        if pred==['Diabetes']:
            return render(request, 'prediction/diabetic.html')
        elif pred==['Pre-Diabetes']:
            return render(request, 'prediction/pre.html')
        else:
            return render(request,'prediction/normal.html')


