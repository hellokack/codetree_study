arr= list(map(int, input().split()))
hap1=0
hap2=0
cnt=0
for i in range(1,10,2):
    hap1 += arr[i]
for i in range(2,11,3):
    hap2 += arr[i]
    cnt+=1
print(hap1, hap2/cnt)
