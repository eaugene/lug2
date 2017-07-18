import csv
import collections

dic = collections.OrderedDict()
with open("fruits.csv", "r+") as fil:
    read_csv1 = csv.reader(fil)
    for row in read_csv1:
        dic['fruits'] = row[0:]
fil.close()

with open("number.csv", "r+") as fil:
    read_csv2 = csv.reader(fil)
    for row in read_csv2:
        dic['number'] = row[0:]
fil.close()

with open("price.csv", "r+") as fil:
    read_csv3 = csv.reader(fil)
    for row in read_csv3:
        dic['price'] = row[0:]
fil.close()

with open("rotten.csv", "r+") as fil:
    read_csv4 = csv.reader(fil)
    for row in read_csv4:
        dic['rotten'] = row[0:]
fil.close()



for e in range(0, 99):
    print(str(dic['number'][e])+" "+str(dic['fruits'][e])+" "+str(dic['price'][e])+" "+str(dic['rotten'][e]))
