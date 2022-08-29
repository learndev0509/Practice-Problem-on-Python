
'''
from itertools import product

d ={'1':['a','b'], '2':['c','d']}

for x, y in product(*d.values()):
    print(x+y)
'''



dt= {'1':['a', 'b'], '2':['c', 'd']}
l=list(dt.values())
print(l)
for i in l[0]:
    for j in l[1]:
        print(i+j)
