arr=list(map(int,input().split()))
sum,s=0,0
for i in range(arr[0],arr[1]+1):
    if i%5==0 or i%7==0:
        sum+=i
        s+=1
avg=sum/s
print(f"{sum} {avg:.1f}")