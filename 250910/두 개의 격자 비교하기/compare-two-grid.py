num=list(map(int,input().split()))
arr1=[]
arr2=[]
for i in range(num[0]):
    a=list(map(int,input().split()))
    arr1.append(a)
for i in range(num[0]):
    b=list(map(int,input().split()))
    arr2.append(b)
for i in range(num[0]):
    for j in range(num[1]):
        if arr1[i][j]==arr2[i][j]:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()