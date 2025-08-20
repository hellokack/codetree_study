arr=list(input().split())
a=len(arr[0])
b=len(arr[1])
if a>b:
    print(arr[0],a)
elif a==b:
    print("same")
else:
    print(arr[1],b)