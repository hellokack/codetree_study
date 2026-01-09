a=list(input().split())
b=list(input().split())
c=list(input().split())
if a[0]=="Y" and int(a[1])>=37:
    if b[0]=="Y" and int(b[1])>=37:
        print("E")
    elif c[0]=="Y" and int(c[1])>=37:
        print("E")
    else:
        print("N")
elif b[0]=="Y" and int(b[1])>=37:
    if c[0]=="Y" and int(c[1])>=37:
        print("E")
    else:
        print("N")
else:
    print("N")