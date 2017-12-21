from collections import namedtuple
ntuple=namedtuple('Human','name age school')
itemp={'name':'lenus','age':24,'school':'zhejiang unviersity'}
ntupobj=ntuple(**itemp)
ntupobj=ntuple(name='lenus',age=24,school='zhejiang university')
ntupobj=ntuple('lenus',24,'zhejiang university')
print(ntupobj)