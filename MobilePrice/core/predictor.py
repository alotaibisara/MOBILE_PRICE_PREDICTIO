# from pandas
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.metrics import accuracy_score
from core.models import TrainModel
from django_pandas.io import read_frame


class Predictor:
    def __init__(self):
        qs = TrainModel.objects.all()
        data = read_frame(qs,coerce_float=True)
        data = data.drop('id',axis=1)
        x = data.iloc[:, :-1].values
        y = data.iloc[:, -1].values
        self.s = StandardScaler()
        x = self.s.fit_transform(x)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)
        self.lreg = LogisticRegression()
        self.lreg.fit(x_train, y_train)
        y_pred =  self.lreg.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred) * 100








