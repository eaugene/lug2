import csv
import collections
the=collections.OrderedDict()
noe=[]
dic = collections.OrderedDict()
fin=collections.OrderedDict()
nos=-1

with open("number.csv", "r+") as fil:
    read_csv1 = csv.reader(fil)
    for row in read_csv1:
        dic['id'] = row[0:]
fil.close()

with open("fruits.csv", "r") as fil:
    read_csv1 = csv.reader(fil)
    for row in read_csv1:
        dic['fruits'] = row[0:]
fil.close()

with open("price.csv", "r") as fil:
    read_csv3 = csv.reader(fil)
    for row in read_csv3:
        dic['price'] = row[0:]
fil.close()

with open("rotten.csv", "r") as fil:
    read_csv4 = csv.reader(fil)
    for row in read_csv4:
        dic['rotten'] = row[0:]
fil.close()
nos=-1
for e,f,g,h in zip(dic['id'],dic['fruits'],dic['price'],dic['rotten']):
    nos=nos+1
    the[nos]=[e,f,g,h]
nos=-1
for t in the.keys():
    nos=nos+1
    if not (len(str(the[t][0]))>0):
        if(nos%2==0):
            noe.append(nos)
        else:
            the[t][0]=nos
for e in noe:
    del the[e]
nos=-1
for h in the.keys():
    nos=nos+1
    fin[nos]=[str(the[h][0]),str(the[h][1]),str(the[h][2]),str(the[h][3])]
for h in fin.keys():
    if(len(str(fin[h][1]))==0):
        y=int(fin[h][0])
        if (0 <= y and y < 10):
            y = (y - 10) % int(len(fin))
        else:
            y = y - 10
        if(len(str(fin[y][1]))==0):
            yi=y
            if (0 <= y and y < 10):
                y = (y - 10) % int(len(fin))
            else:
                y = y - 10
            fin[yi][1] = str(fin[y][1])
        fin[h][1]=str(fin[y][1])
    if (len(str(fin[h][2])) <= 0):
        fin[h][2] = float(0)
    else:
        fin[h][2] = float(fin[h][2])
for k in fin.keys():
    if(fin[k][3]==str(0) or fin[k][3]==str('f')):
        fin[k][3]=str('f')
        fin[k][2]=float(0)
    elif(fin[k][3]==str(1) or fin[k][3]==str('t')):
        fin[k][3]=str('t')
with open('data.csv','w') as p:
    writ=csv.writer(p)
    for j in fin.keys():
        writ.writerow([str(fin[j][0]),str(fin[j][1]),str(fin[j][2]),str(fin[j][3])])
p.close()