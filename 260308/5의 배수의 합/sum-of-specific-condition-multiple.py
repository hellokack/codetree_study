arr=list(map(int,input().split()))
sum=0
if arr[0]<arr[1]:
    for i in range(arr[0],arr[1]+1):
        if i%5==0:
            sum+=i
else:
    for i in range(arr[1],arr[0]+1):
        if i%5==0:
            sum+=i
print(sum)