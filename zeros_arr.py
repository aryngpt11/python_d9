"""from numpy import *
a=zeros(5,)
print(*a)
  """

""" from numpy import *
a=ones(5,dtype=int)
print(*a) """

""" from numpy import*
a=array([10,20,30,40,50,60])
b=array([100,200,300,400,500,600])
c=a+b
print(*c) """


#all and any function


""" from numpy import*
a=array([100,200,300,400,500,600])
b=array([100,200,30,40,500,600])
c=a==b
print(any(c))
print(all(c)) """

#where function

""" from numpy import*
a=array([100,200,300,400,500,600])
b=array([100,200,30,40,500,600])
c=where(a>b,a,b)
print(c) """

#nonzero function

""" from numpy import*
a=array([100,200,300,0,400,500,600])
c=nonzero(a)
print(c) """


##view method


from numpy import*
a=array([10,20,30,40,50])
b= a.view()
array.append(109)
print(a)
print(b)