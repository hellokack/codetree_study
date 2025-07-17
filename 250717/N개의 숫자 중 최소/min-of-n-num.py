import sys
n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min=sys.maxsize
for i in a:
    if min > i:
        min = i
    

cnt=a.count(min)
print(min, cnt)