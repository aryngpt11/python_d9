""" from numpy import*
a=int(input("Enter no of elements: "))
n=zeros(a,dtype=int)
for i in range(a):
    p=int(input("Enter Element"))
    n[i]=p
for i in range(a):
    print(n[i]) """


from numpy import*
a=int(input("Enter no of elements: "))
n=zeros(a,dtype=int)
i=0
j=0
while(i<a):
    x=int(input("Enter the Element: "))
    n[i]=x
    i+=1
while(j<a):
    print(n[j])
    j+=1

