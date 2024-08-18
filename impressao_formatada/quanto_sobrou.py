qtd1=int(input())
qtd2=int(input())
qtd3=int(input())

vl1=float(input())
vl2=float(input())
vl3=float(input())

dinheiro=float(input())

valortotal=qtd1*vl1+qtd2*vl2+qtd3*vl3
troco=dinheiro-valortotal

print("{:.2f}".format(troco))