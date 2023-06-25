from numpy import*
m=int(input("Enter the row: "))
n=int(input("Enter the column: "))
a=zeros((m,n),dtype=int)
print(a)
u=len(a)
i=0
while(i<u):
    j=0
    while(j<len(a[i])):
        x=int(input("Enetr the value of element: "))
        a[i][j]=x
        j+=1
    i+=1
i=0
while(i<u):
    j=0
    while(j<len(a[i])):
        print(a[i][j])
        j+=1
    i+=1
print(a)