num=int(input())
arr=list(map(int, input().split()))
arr_count= [0]*10
for e in arr:
    arr_count[e] +=1
           
for i in range(1,10):
    cnt = arr_count[i]
    print(cnt)