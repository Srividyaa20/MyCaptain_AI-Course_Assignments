# -*- coding: utf-8 -*-
"""Task - 5(Dataset Classification).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HfZzkhK4sEJFX0Nm1IAY5sykO818jziE
"""

import sys
print('Python: {}'.format(sys.version))
import scipy
print('Scipy: {}'.format(scipy.__version__))
import numpy
print('Numpy: {}'.format(numpy.__version__))
import matplotlib
print('Matplotlib: {}'.format(matplotlib.__version__))
import pandas
print('Pandas: {}'.format(pandas.__version__))
import sklearn
print('Sklearn: {}'.format(sklearn.__version__))

import pandas
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.ensemble import VotingClassifier

"""Load the dataset and understand it's statistical summaries and data visualization"""

# loading the dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
names = ['sepal-lenght', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names = names)

# dimension of the dataset
print(dataset.shape)

# take a peek at the data
print(dataset.head(20))

# statiscal summary
print(dataset.describe())

# class distribution
print(dataset.groupby('class').size())

# univariate plots - box and whisker plots
dataset.plot(kind = 'box', subplots = True, layout = (2,2), sharex = False, sharey = False)
pyplot.show()

# histogram of the variable
dataset.hist()
pyplot.show()

# multivariate plots
scatter_matrix(dataset)
pyplot.show()

# creating a validation dataset
# splitting dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, train_size = 0.2, random_state = 1)

"""Create 6 ML models"""

# Logistic Regression
# Linear Discriminant Analysis
# K-Nearest Neighbors
# Classification and Regression Trees
# Gausian Naive Bayes
# Support vector Machines

# Bulding models
models = []
models.append(('LR', LogisticRegression(solver = 'liblinear', multi_class = 'ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate the created models
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits = 7, random_state = 1, shuffle = True)
    cv_results = cross_val_score(model, X_train, Y_train, cv = kfold, scoring = 'accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
LR: 0.907143 (0.108327)
LDA: 0.964286 (0.087482)
KNN: 0.935714 (0.102519)
NB: 1.000000 (0.000000)
SVM: 0.971429 (0.069985)

# compare our model
pyplot.boxplot(results, labels=names)
pyplot.title('Alogorithm Comparision')
pyplot.show()

# make predictions on svm
model = SVC(gamma = 'auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

# evaluate our predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))