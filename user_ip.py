""" from array import*
roll=array('i',[])
n=int(input("Enter the no of elements: "))
for j in range(n):
    roll.append(int(input("Enter element: ")))
 #for j in range(len(roll)):
    #print(roll[j]) 
for j in roll:
    print(j) """


""" from array import*
roll=array('i',[])
n=int(input("Enter the no of elements: "))
i=0
j=0
while i<n:
    roll.append(int(input("Enter element: ")))
    i+=1
while(j<len(roll)):
    print(roll[j],end=" ")
    j+=1 """
    
#index()method

from array import*
roll=array('i',[10,20,30,40,50,60])
print(roll.index(10))