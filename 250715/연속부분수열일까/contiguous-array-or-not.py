a,b = map(int, input().split())
a_list=list(map(int, input().split()))
b_list=list(map(int, input().split()))
ct=0
cnt=0
for i in range(a-1):
    for j in range(b-1):
        if a_list[i] == b_list[j]:
            if a_list[i+j] == b_list[j+1]:
                ct+=1
                cnt+=1
                break
    if ct ==1:
        break
if cnt==1:
    print("Yes")
else:
    print("No")