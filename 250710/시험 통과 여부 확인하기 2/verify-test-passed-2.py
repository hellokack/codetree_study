stu_len=input()
stu=[]
for j in range(int(stu_len)):
    score = list(map(int, input().split()))
    stu.append(score)
hap=[]
cnt=0
for i in stu:
    if sum(i)/4 >= 60:
        print("pass")
        cnt+=1
    else:
        print("fail")

print(cnt)
