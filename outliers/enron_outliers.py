#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
from sklearn import linear_model
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL')
data = featureFormat(data_dict, features)


### your code below

# reg = linear_model.LinearRegression()
# reg.fit()
# print data_dict
for data1 in data_dict:
	# print data1
	salary= data_dict[data1]['salary']
	bonus = data_dict[data1]['bonus']
	if salary==26704229:
		print data1
	if salary > 1000000 and bonus > 5000000 and salary!='NaN' and bonus!='Nan':
		print data1 + str(data_dict[data1])
# 0e+07   9.73436190e+07

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()