num=int(input())
arr=[]
for i in range(1,num+1):
    if i%2==1:
        for j in range(1,num+1):
            print(j,end="")
    else:
        for j in range(num,0,-1):
            print(j,end="")
    print()