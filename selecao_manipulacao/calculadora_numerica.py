a=int(input())
b=int(input())
op=input()
r=0

if op=='+':
    r=a+b
elif op=='-':
    r=a-b
elif op=='*':
    r=a*b
elif op=='/':
    r=a//b

print(r)


