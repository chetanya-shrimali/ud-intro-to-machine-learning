import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

# data
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# labels
Y = np.array([1, 1, 1, 2, 2, 2])

clf = GaussianNB()

pred = clf.fit(X, Y)
print(clf.predict([[8, 3]]))


y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]
# checks accuracy of predictions
print(accuracy_score(y_true, y_pred))
