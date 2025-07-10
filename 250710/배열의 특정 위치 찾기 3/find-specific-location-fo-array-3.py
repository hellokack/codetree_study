arr = list(map(int, input().split()))
b=[]
for i in arr:
    if i ==0:
        break
    b.append(i)
print(b[-1]+b[-2]+b[-3])
    
