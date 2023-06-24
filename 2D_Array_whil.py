from numpy import*
a=array([[10,20,30,40,50],[60,70,80,90,100]])
n=len(a)
i=0
while i<n:
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    i+=1
    print()