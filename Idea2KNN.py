# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 23:48:22 2017

@author: Saiteja Sirikonda
@Course: Statistical Machine Learning, Fall 2017
Arizona State University


Recommendations based on K- Nearest Neighbors with Euclidean Distance as the
Similarity Metric.

"""
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np


labels = pd.read_csv('Labels.csv')
features = pd.read_csv('Features.csv')

def predict(X_train, y_train, x_test, k):
	# create list for distances and targets
    distances = []
    targets = []
    for i in range(len(X_train)):
		# first we compute the euclidean distance
        distance = np.sqrt(np.sum(np.square(x_test - X_train[i, :])))
		# add it to list of distances
        distances.append([distance, i])
    distances = sorted(distances)
	# make a list of the k neighbors' targets
    for i in range(k):
        index = distances[i][1]
        targets.append(y_train[index][0])
    return targets

def kNearestNeighbor(X_train, y_train, X_test, predictions, k):
    for i in range(len(X_test)):
        predictions.append(predict(X_train, y_train, X_test[i, :], k))
    return predictions
        

accuracy_for_eachK = []
count_arr = []
for K in [7,9]:
    accuracy_for_each_fold = []
    print "K Values:",K
    for b in [5,10]:
        X_train, X_test, y_train, y_test = train_test_split(np.array(features),np.array(labels),test_size=0.1)
        predictions,count = [],0
        print "B Values:",b
        kNearestNeighbor(X_train, y_train, X_test, predictions, K)
        for i in xrange(len(predictions)):
            if y_test[i] in predictions[i]:
                count+=1
        count_arr.append(count);
        print count
        print count*1.0/len(predictions)*100.0
        accuracy_for_each_fold.append((count*1.0/len(predictions))*100.0)
    accuracy_for_eachK.append(sum(accuracy_for_each_fold))
    print accuracy_for_eachK

                
            
 


































