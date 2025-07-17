import sys
n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max= -sys.maxsize
for i in a:
    if i > max:
        max = i
a.remove(max)
max2= -sys.maxsize
for i in a:
    if i > max2:
        max2 = i
print(max, max2)
