arr = list(map(int, input().split()))
h=[]
j=[]
for i in range(0,10,2):
    h.append(arr[i])
for i in range(1,10,2):
    j.append(arr[i])
sum_h=sum(h)
sum_j=sum(j)
if sum_h > sum_j:
    print(sum_h-sum_j)
else:
    print(sum_j-sum_h)