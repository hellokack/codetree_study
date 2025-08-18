import sys
num=list(map(int,input().split()))
num1=-sys.maxsize
num2=-sys.maxsize
for i in range(3):
    if num[i]>num1:
        num1=num[i]
for i in range(3):
    if num1>num[i]>num2:
        num2=num[i]
print(num2)
