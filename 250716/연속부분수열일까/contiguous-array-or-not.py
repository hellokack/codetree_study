a,b = map(int, input().split())
a_list=list(map(int, input().split()))
b_list=list(map(int, input().split()))

cnt=0
for i in range(a-b+1):
    ct=0
    for j in range(b):
        if a_list[i+j] != b_list[j]:
            ct+=1
            break
    if ct ==0:
        cnt +=1
        break
if cnt==1:
    print("Yes")
else:
    print("No")