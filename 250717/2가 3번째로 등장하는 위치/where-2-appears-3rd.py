num=int(input())
num_list=list(map(int, input().split()))
cnt=0
j=0
for i in num_list:
    j +=1
    if i ==2:
        cnt +=1
    if cnt ==3:
        print(j)
        break