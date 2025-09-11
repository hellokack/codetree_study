arr=[]
for i in range(4):
    a=list(map(int,input().split()))
    arr.append(a)
for i in range(4):
    hap=0
    for j in range(4):
        hap += arr[i][j]
    print(hap)