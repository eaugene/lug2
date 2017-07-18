import csv
import collections
the=collections.OrderedDict()
no=[]
noe=[]
dic = collections.OrderedDict()

nos=-1;
with open("number.csv", "r") as fil:
    read_csv2 = csv.reader(fil)
    nl=list(read_csv2)[0]
    print(nl)
    for e in nl:
        nos=nos+1
        print(e+" "+str(nos))
        if not (len(str(e))>0):
            if not (nos%2==0):
                no.append(nos)
            else:
                no.append(nos)
                noe.append(nos)
    for y in nl:
        print(y)
    for y in no:
        print(y)
    for y in noe:
        print(y)
fil.close()
#rem=-
nos=-1;
with open("fruits.csv", "r+") as fil:
    read_csv1 = csv.reader(fil)
    ml=list(read_csv1)[0]
    for e in ml:

        print(e)
fil.close()

'''with open("price.csv", "r+") as fil:
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
    print(str(dic['number'][e])+" "+str(dic['fruits'][e])+" "+str(dic['price'][e])+" "+str(dic['rotten'][e]))'''

