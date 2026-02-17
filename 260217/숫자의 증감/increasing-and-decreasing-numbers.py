arr=list(input().split())
i=int(arr[1])
if arr[0]=="A":
    for e in range(1,i+1):
        print(e,end=" ")
        e+=1
else:
    for e in range(i,0,-1):
        print(e,end=" ")
        e-=1