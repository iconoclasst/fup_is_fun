p=input()
n=float(input())

if p=='c':
    print(n.__ceil__())
elif p=='r':
    print(n.__round__())
elif p=='f':
    print(n.__floor__())
else:
    print("invalido")