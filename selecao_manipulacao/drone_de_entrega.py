
#dimensões da caixa em centímetros
a = int(input())
b = int(input())
c = int(input())

#altura(h) e largura(l) da janela em centímetros
h = int(input())
l = int(input())

#saída S se a caixa passa pela janela
#saída N se a caixa não passa pela janela

dim = [a*b, a*c, b*c]
jan = h*l

ctt=0
for d in dim:
    if d <= jan:
        print("S")
        break
    else:
        ctt+=1

if ctt==3:
    print("N")
    
#print(dim)






