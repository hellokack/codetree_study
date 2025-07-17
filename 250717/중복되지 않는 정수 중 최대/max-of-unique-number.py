import sys
n = int(input())
nums = list(map(int, input().split()))
new=[]
# Please write your code here.
max=-sys.maxsize
for i in nums:
    if nums.count(i)<2:
        new.append(i)
for i in new:
    if i > max:
        max =i
if new == []:
    print(-1)
else:
    print(max)
