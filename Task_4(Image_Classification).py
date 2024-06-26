# -*- coding: utf-8 -*-
"""Task - 4(Image Classification).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z_Tqz5VBtoS_7i7LfybIWpxMzK7cRSnB

1. Using Iris Flower dataset for our image classification
"""

from sklearn import datasets #importing toy dataset
iris=datasets.load_iris() #loading iris data set
x=iris.data #storing the features
y=iris.target #our target variable
from sklearn.model_selection import train_test_split #time to split data into train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3) #here test data is 30% of our total data and train is 70%
from sklearn import tree #our algorithm
classifier=tree.DecisionTreeClassifier()
classifier.fit(x_train,y_train)
predictions=classifier.predict(x_test) #predicting using features in test model
from sklearn.metrics import accuracy_score #calculating accuracy of the model
print(accuracy_score(y_test,predictions))

"""2. Using Breast Cancer Wisconsin Dataset"""

from sklearn import datasets #importing toy dataset
cancer=datasets.load_breast_cancer() #loading the dataset
x=cancer.data
y=cancer.target
from sklearn.model_selection import train_test_split #time to split data into train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.4) #here test data is 40% of our total data and train is 60%
from sklearn import tree #importing the algorithm
classifier=tree.DecisionTreeClassifier() #decision tree algorithm
classifier.fit(x_train,y_train)
predictions=classifier.predict(x_test) #predicting using features in test model
from sklearn.metrics import accuracy_score #calculating accuracy of the model
print(accuracy_score(y_test,predictions))