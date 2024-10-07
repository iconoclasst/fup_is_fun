v=int(input())
c1=int(input())
c2=int(input())

d1=v-c1
d2=v-c2

if d1<0:
    d1=d1-d1-d1

if d2<0:
    d2=d2-d2-d2

if d1==d2:
    print("empate")

if d1<d2:
    print("primeiro")
elif d1>d2:
    print("segundo")

# print(d1)
# print(d2)