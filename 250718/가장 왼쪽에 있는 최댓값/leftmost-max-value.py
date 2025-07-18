import sys
n = int(input())
a = list(map(int, input().split()))
b=[]
# Please write your code here.

# 
# 0. while(index != 0)
# 1. 배열(0 ~ index)의 최댓값 max의 idx를 찾는 과정
# 2. 0 ~ idx를 배열 A로 쳐서 다시 while문
max_a = len(a)
while max_a != 0:
    idx = 0
    for i in range(max_a) :
        # 최댓값 idx 찾기
        if a[idx] < a[i] :
            idx = i
    
    print(idx + 1, end=" ")
    max_a = idx

# max=-sys.maxsize
# for i in a:
#     if i > max:
#         max= i
# while max!=1: 
#     for i in range (10):
#         for j in range((a.index(max))+1):
#             b.append(a[j])
#             print(b)
#         max=-sys.maxsize
#         for i in b:
#             if i > max:
#                 max= i
# print(b)
