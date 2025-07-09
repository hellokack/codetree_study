score=list(map(float,input().split()))
n=len(score)
hap=0
for i in score:
    hap += i
avg = hap / n
print(avg)