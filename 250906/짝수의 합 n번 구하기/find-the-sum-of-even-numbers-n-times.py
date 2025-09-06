num=int(input())
for i in range(num):
    arr=list(map(int,input().split()))
    hap=0
    for j in range(arr[0],arr[1]+1):
        if j %2==0:
            hap +=j
    print(hap)