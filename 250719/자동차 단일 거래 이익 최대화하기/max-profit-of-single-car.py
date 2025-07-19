n = int(input())
price = list(map(int, input().split()))
max=0
# Please write your code here.
for i in range(n-1,-1,-1):
    for j in range(i,-1,-1):
        if price[i]-price[j]>max:
            max=price[i]-price[j]
print(max)