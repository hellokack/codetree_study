arr=list(map(int, input().split()))
hap=[]
for i in range(10):
    sum=0
    sum=(arr[i]+arr[i+1])%10
    arr.append(sum)
    print(arr[i],end=" ")
