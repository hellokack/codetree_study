arr= list(map(int, input().split()))
cnt=0
hap=0
for i in arr:
    if i == 0:
        break
    cnt +=1
    hap += i
avg = hap/cnt
print(f"{hap} {avg:.1f}")
