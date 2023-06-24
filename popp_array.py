""" from array import *
roll=array('i',[10,11,27,29,14])
n=len(roll)
i=0
while (i<n):
    print(roll[i])
    i+=1

print("Elements after pop")
roll.pop()

n=len(roll)
i=0
while (i<n):
    print(roll[i])
    i+=1
 """

from array import *
roll=array('i',[10,11,27,29,14])
n=len(roll)
i=0
while (i<n):
    print(roll[i])
    i+=1

print("Elements after pop")
r=roll.pop(0)

n=len(roll)
i=0
while (i<n):
    print(roll[i])
    i+=1
print("Removed Element: ",r)
