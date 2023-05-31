import numpy as np
import pandas as pd
import collections

def euclid_distance(x1, x2):
    distance = np.sqrt(np.sum((x1-x2)**2))
    return distance

class KNN():
    def _init(self, k):
        self.k = k
    
    def fit(self,X,y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions
    
    def _predict(self, x):
        for x_train in self.X_train:
            distances = euclid_distance(x, x_train)

        #most common lables of closest k Points
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = collections.Counter(k_nearest_labels).most_common(1)[0][0]
        return most_common