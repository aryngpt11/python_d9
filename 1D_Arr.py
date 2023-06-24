""" import array
roll=array.array('i',[101,102,104,103,105])
print(roll[1])
for i in roll:
    print(i) """

#2nd type

""" import array as aryn
roll=aryn.array('i',[101,102,104,103,105])

for i in roll:
    print(i) """

#3rd type

""" from array import*
roll=array('i',[101,102,104,103,105])

for j in roll:
    print(j)
 """

 #4th type print its index also
from array import*
roll=array('i',[101,102,104,103,105])
n=len(roll)
for j in range(n):
    print(roll[j],j)
 