a,b = list(map(int, input().split()))
cnt=[0]*11
c=0
while a>1:
    c= a%b
    a = a//b
    cnt[c] +=1
hap=0
for i in cnt:
    hap += i*i
print(hap)