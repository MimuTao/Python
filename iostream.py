import csv
import os
if (not os.path.exists('csv')) or (os.path.exists('csv') and (not os.path.isdir('csv'))):
    os.mkdir('csv',0x755)
data=[
    ['zhangsan','24'],
    ['lisi','17'],
    ['ztutu','16'],
]
with open('./csv/csv.csv','wt',newline='') as fout:
    csvout=csv.writer(fout)
    csvout.writerows(data)

with open('./csv/csv.csv','rt') as fin:
    csvin=csv.reader(fin)
    print(list(csvin))

key_data=[
    {'name':'zhangsan','age':25,'school':'zhejiang university'},
    {'name':'zhangqian','age':24,'school':'tinghua university'},
    {'name':'fanmin','age':24,'school':'xinan zhengfa university'},
    {'name':'zhangzexi','age':18,'school':'fudan university'},
]

with open('./csv/key.csv','wt',newline='') as fout:
    head_names=['name','age','school']
    csvout=csv.DictWriter(fout,fieldnames=head_names)
    csvout.writeheader()
    csvout.writerows(key_data)

with open('./csv/data.csv','rt') as fin:
    csvin=csv.DictReader(fin,fieldnames=['id','name'])
    print(csvin.fieldnames)
    result=[i for i in csvin]
    

with open('./csv/key.csv','rt') as fin:
    csvin=csv.reader(fin)
    fieldnames=next(csvin)
    rest=[i for i in csvin]
