num=int(input())
arr=list(map(int, input().split()))
num2=[i for i in arr if i % 2 ==0]
for i in num2:
    print(i, end=' ')