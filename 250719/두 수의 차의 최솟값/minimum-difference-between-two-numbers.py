import sys
n=int(input())
num=list(map(int,input().split()))
min=sys.maxsize
for i in range(n-1,0,-1):
    if num[i]-num[i-1]<min:
        min=num[i]-num[i-1]
print(min)