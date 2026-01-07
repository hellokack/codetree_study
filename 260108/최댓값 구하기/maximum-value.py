arr=list(map(int,input().split()))
max=-200
if arr[0]>max:
    max=arr[0]
if arr[1]>max:
    max=arr[1]
if arr[2]>max:
    max=arr[2]
print(max)