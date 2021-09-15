import csv 
import os

os.system('cls')

f1 = open('merge/bright_stars.csv')
f2 = open('merge/unit_converted_stars.csv')

r1 = csv.reader(f1)
r2 = csv.reader(f2)

data1 = []
data2 = []

for row in r1:
    data1.append(row)

for row in r2:
    data2.append(row)

header1 = data1[0]
header2 = data2[0]

datar1 = data1[1:]
datar2 = data2[1:]

header1[0] = "Index"
header2[0] = "Index"

#print(header1)
#print(header2)

#testing

fheader = header1
print(fheader)

fdata = []

for row in datar1:
    fdata.append(row)

for row in datar2:
    row.append("N/A") 
    row[0] = int(row[0]) + int(len(datar1))
    fdata.append(row)

with open('merge/merge2.csv','w') as f:
    r = csv.writer(f)
    r.writerow(fheader)
    r.writerows(fdata)