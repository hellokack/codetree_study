arr= list(map(int, input().split()))

for i in arr:  
    if i %2 == 0:
        i= i/2
    else:
        i+=3
    if i == 0:
        break
    print(int(i),end=' ')