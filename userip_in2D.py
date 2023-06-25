from numpy import*
m=int(input("Enter no.of rows: "))
n=int(input("Enter no.of colmns: "))
a=zeros((m,n),dtype=int) 
u=len(a)
for i in range(u):
    for j in range(len(a[i])):
        x=int(input("Enter elements: "))
        a[i][j]=x
for i in range(u):
    for j in range(len(a[i])):
        print(a[i][j])
    print()
print(a)
