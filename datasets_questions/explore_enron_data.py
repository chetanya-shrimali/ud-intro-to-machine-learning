#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
count=0
nan_count=0
total_count=0
nan_poi_count = 0
for data in enron_data:
	total_count += 1
	if enron_data[data]['total_payments']=='NaN':
		nan_count += 1

	poi = enron_data[data]['poi']
	if poi is not False:
		if enron_data[data]['total_payments']=='NaN':
			nan_poi_count += 1
		print data
		count += 1
print count
print total_count
print nan_count
print nan_poi_count	
percent = float(nan_count)/float(total_count)
print percent
# print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# names = open("../final_project/poi_names.txt", "r")
# for name in names:
# 	print name[4:20]