import sys
n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
max=-sys.maxsize
for i in nums:
    if nums.count(i)>=2:
        for j in range(nums.count(i)):
            nums.remove(i)
for i in nums:
    if i > max:
        max =i
if nums == []:
    print(-1)
else:
    print(max)
