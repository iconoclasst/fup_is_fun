seg=int(input())

hr=seg // 3600
resto=seg%3600
min=resto//60
seg=resto%60


print("{:02d}:{:02d}:{:02d}".format(hr,min,seg))
