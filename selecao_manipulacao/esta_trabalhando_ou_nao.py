#ESTÁ TRABALHANDO: segunda à sexta (8h - 11; 14h - 17h); sábado (8h - 11)

dia=int(input())
hora=int(input())

#Domingo
if dia == 1:
    print("NAO")
#Segunda à sexta
elif ((hora >= 8 and hora <= 11) or (hora >= 14 and hora <= 17)) and (dia != 1 and dia != 7):
    print("SIM")
#Sábado
elif dia == 7 and (hora >= 8 and hora <= 11): 
    print("SIM")
else:
    print("NAO")


