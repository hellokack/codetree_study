arr=[
    list(map(int,input().split()))
    for _ in range(2)
    
]
avg_1=0
for i in range(2):
    avg_g=0
    for j in range(4):
        avg_g+=arr[i][j]
    avg_1 += avg_g
    print(avg_g/4,end=' ')
print()
for j in range(4):
    avg_s=0
    avg_s=arr[0][j] + arr[1][j]
    print(avg_s/2,end=' ')
print()
print(avg_1/8)
    