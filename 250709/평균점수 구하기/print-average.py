score=list(map(float,input().split()))
cnt=0
hap=0
for j in score:
    if j>=100:
        break
    hap += j
    cnt += 1
avg = hap / cnt
print(f"{avg:.1f}")