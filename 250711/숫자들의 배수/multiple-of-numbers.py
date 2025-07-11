arr=list(map(int, input()))
arr= [arr[0]*i for i in range(1,30)]
cnt=0
arr2=[]
for i in arr:
    print(i, end=' ')
    if i %5 ==0:
        cnt+=1
    if cnt == 2:
        break
    
