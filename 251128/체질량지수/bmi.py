arr=list(map(int,input().split()))
b=10000*arr[1]/arr[0]**2
if b>=25:
    print(int(b//1))
    print("Obesity")
else:
    print(int(b//1))