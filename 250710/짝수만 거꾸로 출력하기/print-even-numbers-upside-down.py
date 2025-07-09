num_len=input()
num=list(map(int, input().split()))
res=[]
for i in num:
    if i %2 == 0:
        res.append(i)
for i in range(len(res)-1,-1,-1):
    print(res[i], end = ' ')
