num=int(input())
arr=[[0 for _ in range(num)]for _ in range(num)]
for i in range(num):
    for j in range(num):
        if i%2==1:
            arr[j][i]=num-j
        else:
            arr[j][i]=j+1
for row in arr:
    print("".join(map(str, row)))