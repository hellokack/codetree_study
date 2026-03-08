arr=list(map(int,input().split()))
sum=0
for i in range(arr[0],arr[1]):
    if i%2==0:
        sum+=i
print(sum)