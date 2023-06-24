from array import*
roll=array('i',[101,102,104,103,105])
roll.append(109)
n=len(roll)

for j in range(n):
    print(roll[j],j)