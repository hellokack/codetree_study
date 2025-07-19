arr=list(map(int, input().split()))
max=0
min=1000
for i in arr:
    if i <500:
        if i>max:
            max =i
    else:
        if i<min:
            min =i
print(max, min)