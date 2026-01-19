arr=list(map(int,input().split()))
ans=0
if arr[0]>arr[1]>arr[2]or arr[2]>arr[1]>arr[0]:
    ans=arr[1]
elif arr[0]>arr[2]>arr[1]or arr[1]>arr[2]>arr[0]:
    ans=arr[2]
elif arr[2]>arr[0]>arr[1]or arr[1]>arr[0]>arr[2]:
    ans=arr[0]
print(ans)