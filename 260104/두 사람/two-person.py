a=list(input().split())
b=list(input().split())
if int(a[0])>=19 and int(b[0])>=19:
    if a[1]=="M" or b[1]=="M":
        print(1)
    else:
        print(0)