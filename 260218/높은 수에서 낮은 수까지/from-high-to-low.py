arr=list(map(int,input().split()))
if arr[0]>arr[1]:
    for i in range(arr[0],arr[1]-1,-1):
        print(i,end=" ")
else:
    for i in range(arr[1],arr[0]-1,-1):
        print(i,end=" ")