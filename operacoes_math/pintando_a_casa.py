from math import sqrt

l1=float(input())
l2=float(input())
l3=float(input())

p=(l1+l2+l3)/2
a=sqrt(p*(p-l1)*(p-l2)*(p-l3))

print("{:.2f}".format(a))
