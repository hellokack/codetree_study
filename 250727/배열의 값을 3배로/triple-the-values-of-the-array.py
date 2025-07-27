arr=[]
a=[0,0,0]
for i in range(3):
    a[i]=list(map(int, input().split()))
    arr.append(a[i])
arr_w=[]
for i in range(3):
    w=[]
    for j in range(3):
        w.append(arr[i][j]*3)
    arr_w.append(w)
for i in range(3):
    for j in range(3):
        print(arr_w[i][j],end=" ")
    print()