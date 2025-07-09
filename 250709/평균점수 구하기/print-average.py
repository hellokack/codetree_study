score=list(map(float,input().split()))
n=len(score)
hap=0
for j in range(n):
    if score[j]>=100:
        break
for i in score:
    hap += i
avg = hap / n
print(avg)