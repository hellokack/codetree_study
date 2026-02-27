five=0
thr=0
for i in range(10):
    a=int(input())
    if a%3==0:
        thr+=1
    if a%5==0:
        five+=1
print(thr,five)