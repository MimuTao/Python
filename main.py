# mdict = {
#     'name': 'lihua',
#     'age': 23,
#     'school': 'zhejiang university'
# }
# mdict={
#     'second':2,
#     'first':1,
#     'third':3,
# }
# new_dict=sorted(mdict.items(),key=lambda item:item[1])
from Library.run import Human,PI
import math

print(math.floor(3.13))
print(math.ceil(3.13))
print(int(3.134))
print(PI)
host=Human('lihua',23)
print(host.GetAge())
print(host.GetName())
print(host._age)
print('hello','world',sep='-')
print(int('010',base=8))
print(int('0xF',base=16))
