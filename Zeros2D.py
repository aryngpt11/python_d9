""" from numpy import*
a=zeros((3,2),dtype=int)
for i in a:
    for j in i:
        print(j)
    print()
 """
 #ones function
""" from numpy import*
a=ones((3,2),dtype=int)
for i in a:
    for j in i:
        print(j)
    print() """

#reverse function()

""" from numpy import*
a=array([1,2,3,4,5,6,7,8,9,10,11,12])
b=reshape(a,(2,3,2))
print(a)
print(b) """

#flatten()method
from numpy import*
a=array([[1,2,3,4,5],[6,7,8,9,10]])
b=a.flatten()
print(b)
        
 