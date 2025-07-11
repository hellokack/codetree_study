num=int(input())
arr=[0,0]
for i in range(2,100):
    arr[0]=1
    arr[1]=num
    arr.append(arr[-1]+arr[-2])
    if arr[i] >=100:
        break
for i in arr:
    print(i, end=' ')