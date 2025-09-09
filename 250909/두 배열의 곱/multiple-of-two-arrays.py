arr1=[]
arr2=[]
arr3=[]
for i in range(3):
    a=list(map(int,input().split()))
    arr1.append(a)
c=input()
for i in range(3):
    b=list(map(int,input().split()))
    arr2.append(b)
for i in range(3):
    for j in range(3):
        print(arr1[i][j]*arr2[i][j],end=" ")
    print()