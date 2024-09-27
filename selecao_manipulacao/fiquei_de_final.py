n1=int(input())
n2=int(input())
nf=int(input())
media=(n1+n2)/2

if media >= 7:
    print("Aprovado")
elif media < 4:
    print("Reprovado")
else:
    mediafinal=(media+nf)/2
    if mediafinal >= 5:
        print("Aprovado na final")
    else:
        print("Reprovado na final")
