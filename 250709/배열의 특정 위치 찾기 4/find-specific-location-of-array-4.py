arr = list(map(int, input().split()))
res=[]
cnt=0
for i in arr:
    if i ==0:
        break
    if i %2 == 0:
        res.append(i)
        cnt +=1

print(cnt, sum(res))
