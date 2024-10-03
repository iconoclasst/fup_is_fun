l1 = int(input())
l2 = int(input())
l3 = int(input())

sums=[l1+l2, l1+l3, l2+l3]
   
for s in sums:
    if l1 > s or l2 > s or l3 > s:
        print("False")
        break
    else:
        print("True")
        break