import csv
import collections
import matplotlib.pyplot as p
no = []
pri = []
with open("data.csv","r") as c:
	read = csv.reader(c)
	for y in read:
		if(len(y)>0):
			no.append(int(y[0]))
			pri.append(float(y[2]))