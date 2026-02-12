arr=list(map(int,input().split()))
i=arr[0]
while arr[0]>=i and arr[1]<=i:
    if i%2==0:
        print(i,end=" ")
    i-=1
    