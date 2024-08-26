valor=int(input())
parcelas=int(input())

juros=0

if parcelas == 2:
    juros=valor*5/100
elif parcelas == 3:
    juros=valor*10/100
elif parcelas == 4:
    juros=valor*15/100
elif parcelas == 5:
    juros=valor*20/100
elif parcelas == 6:
    juros=valor*25/100
elif parcelas == 7:
    juros=valor*30/100
elif parcelas == 8:
    juros=valor*35/100
elif parcelas == 9:
    juros=valor*40/100
elif parcelas == 10:
    juros=valor*45/100

valor_parcela=(valor+juros)/parcelas
valor_total=valor_parcela*parcelas

print("{:.2f}".format(valor_parcela))
print("{:.2f}".format(valor_total))

