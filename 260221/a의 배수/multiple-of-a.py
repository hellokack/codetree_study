arr=list(map(int,input().split()))
i=1
while i<=arr[0]:
    if i%arr[1]==0:
        print(1)
    else:
        print(0)
    i+=1