num=int(input())
num2=list(map(int,input().split()))
for i in range(num-1,-1,-1):
    if num2[i]%2 ==0:
        print(num2[i],end=' ')
