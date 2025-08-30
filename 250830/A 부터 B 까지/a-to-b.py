num=list(map(int,input().split()))
a=num[0]
b=num[1]
while a<=b:
    print(a,end=' ')
    if a%2==0:
        a+=3
    else:
        a*=2
    