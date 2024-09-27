wifi=bool(int(input()))
login=bool(int(input()))
admin=bool(int(input()))


if not wifi:
    print("you must connect to wifi")
elif not login:
    print("you need to login first")
elif not admin:
    print("you must to login as admin")
else:
    print("done")
