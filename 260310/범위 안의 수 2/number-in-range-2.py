sum=0
e=0
for i in range(10):
    a=int(input())
    if a>=0 and a<=200:
        sum+=a
        e+=1
print(f"{sum} {sum/e:.1f}")