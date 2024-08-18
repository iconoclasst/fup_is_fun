hr=int(input())
min=int(input())
dia=int(input())
mes=int(input())
ano=int(input())
ano = ano % 100

print("{:02d}:{:02d} {:02d}/{:02d}/{}".format(hr, min, dia, mes, ano))