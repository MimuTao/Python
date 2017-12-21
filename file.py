import os
import csv

ilist=[
    ['1','zhangling','zhejiang university','23'],
    ['2','liyiqun','zhejiang university','26'],
    ['3','zhangtutu','zhejiang university','18'],
    ['4','zhangzexi','zhejiang university','24'],
]
with open('./csv/keycsv.csv','wt') as fin:
    fin.write('id,name,school,age\n')
    for i in ilist:
        rest=','.join(i)
        fin.write(rest+'\n')
        # print(rest,file=fin)

with open('./csv/keycsv.csv','rt') as fin:
    csvin=csv.DictReader(fin)
    for i in csvin:
        print(i)

with open('./csv/keycsv.csv','rt') as fin:
    csvin=csv.reader(fin)
    fieldnames=next(csvin)
    rest=[i for i in csvin]

with open('./csv/keycsv.csv',mode='rt') as fin:
    fieldnames_string=fin.readline()
    print(fieldnames_string.strip('\n').split(','))
    for i in fin.readlines():
        print(i.strip('\n').split(','))
    # print(fin.readlines())
