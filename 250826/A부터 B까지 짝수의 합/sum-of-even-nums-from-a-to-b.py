num=list(map(int,input().split()))
cnt=0
for i in range(num[0],num[1]+1):
    if i %2==0:
        cnt += i
print(cnt)