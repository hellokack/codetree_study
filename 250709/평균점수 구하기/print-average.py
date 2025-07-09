score=list(map(float,input().split()))
n=len(score)
hap=0
for j in score:
    if j>=100:
        break
    hap += j
avg = hap / n
print(avg)