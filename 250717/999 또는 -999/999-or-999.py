import sys
arr = list(map(int, input().split()))
max=-sys.maxsize
min=sys.maxsize
for i in arr:
    if i == 999 or i == -999:
        break
    if i >max:
        max=i
    if i <min:
        min =i
print(max, min)