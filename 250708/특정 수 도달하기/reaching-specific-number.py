num = input().split()
hap=0
cnt=0
for i in num:
    if int(i) >= 250:
        break
    hap += int(i)
    cnt += 1
avg_num=hap/cnt
print(hap,avg_num)

