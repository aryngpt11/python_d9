""" import numpy as np
roll=np.array([[10,30,20,50,40],[80,90,70,100,110]])
print(roll)
print(type(roll)) """

#without index
""" from numpy import*
roll=array([[10,30,20,50,40],[80,90,70,100,110]])
for i in roll:
    for j in i:
        print(j)
    print() """

#with index
from numpy import*
a=array([[10,30,20,50,40],[80,90,70,100,110]])
n=len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j])
    print()