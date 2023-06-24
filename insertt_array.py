""" from array import*
roll=array('i',[101,102,104,103,105])
n=len(roll)
i=0
while (i<n):
    print(roll[i])
    i+=1
print("Array after insert: ")
roll.insert(1,108)
roll.insert(2,109)
n=len(roll)
i=0
while (i<n):
    print(roll[i])
    i+=1
 """
#usig for loop


from array import*
roll=array('i',[101,102,104,103,105])
n=len(roll)
for i in range(n):
    print(roll[i],i)

print("Array after insertion: ")
roll.insert(1,108)
roll.insert(2,109)
roll.append(1000)
n=len(roll)
for i in range(n):
    print(roll[i],i)
