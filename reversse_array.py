""" from array import *
roll=array('i',[10,11,27,29,14])
n=len(roll)
i=0
while (i<n):
    print(roll[i])
    i+=1

print("Elements after reverse")
r=roll.reverse()

n=len(roll)
i=0
while (i<n):
    print(roll[i])
    i+=1 """

#extend method
from array import *
roll=array('i',[10,11,27,29,14])
arr=array('i',[14,10,11,27,29])
n=len(roll)
i=0
while (i<n):
    print(roll[i])
    i+=1

print("Elements after extend")
roll.extend(arr)

n=len(roll)
i=0
while (i<n):
    print(roll[i])
    i+=1