arr=list(map(int,input().split()))
i=arr[0]
while i<=arr[1]:
    print(i,end=" ")
    if i%2==1:
        i*=2
    else:
        i+=3
