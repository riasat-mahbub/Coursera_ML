# -*- coding: utf-8 -*-
"""week3_ml

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zv-OYE_LiJNEjYeOjCpR9Kc6lqxxYnt3

Dummy Classifiers

A dummy classifier doesnt actually look at data, but rather predicts by a simple stratagey

It is used to benchmark other classifier models
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.dummy import DummyClassifier

fruit = pd.read_table('fruit_colors.txt')
x = fruit[['mass', 'width', 'height']]
y = fruit['fruit_label']

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 0)

svm = SVC(kernel = 'rbf', C=4).fit(x_train, y_train)
dummy = DummyClassifier(strategy='most_frequent').fit(x_train, y_train)

print('svm accuracy', svm.score(x_test, y_test))
print('dummy accuracy', dummy.score(x_test, y_test))

"""**Confusion Matrix**

Confusion Matrix with Dummy Classifier
"""

from sklearn.dummy import DummyClassifier
from sklearn.metrics import confusion_matrix

dummy = DummyClassifier(strategy='most_frequent').fit(x_train, y_train)
y_predict = dummy.predict(x_test)
confusion = confusion_matrix(y_test, y_predict)
confusion, dummy.score(x_test, y_test)

"""With a SVC"""

from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

svm = SVC(kernel='rbf', C=3).fit(x_train, y_train)
y_predict = svm.predict(x_test)
confusion = confusion_matrix(y_test, y_predict)
confusion, svm.score(x_test, y_test)

"""With a logistic regressor"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

logis = LogisticRegression().fit(x_train, y_train)
y_predict = logis.predict(x_test)
confusion = confusion_matrix(y_test, y_predict)
confusion, logis.score(x_test, y_test)

"""**Other metrics**

Recall -> When we would rather have a false positive than risk a false negative

Precision -> When we would rather have a false negative than risk any kind of false positive

F1 score -> harmonic mean of recall and precision

Below we use the previous logistic regressor to show these scores
"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression

y_train = y_train.map(lambda x: 1 if x==1 else 0)
y_test = y_test.map(lambda x: 1 if x==1 else 0)

logis = LogisticRegression().fit(x_train, y_train)
y_predict = logis.predict(x_test)

print('accuracy', accuracy_score(y_test, y_predict))
print('recall', recall_score(y_test, y_predict))
print('precision', precision_score(y_test, y_predict))
print('f1', f1_score(y_test, y_predict))