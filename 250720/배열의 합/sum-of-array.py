arr=[]
for i in range(4):
    s=list(map(int,input().split()))
    arr.append(s)
    print(sum(arr[i]))