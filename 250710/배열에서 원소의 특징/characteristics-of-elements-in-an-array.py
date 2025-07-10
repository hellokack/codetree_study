arr= list(map(int, input().split()))
num=[]
for i in arr:
    if i %3==0:
        break
    else:
        num.append(i)
print(num[-1])