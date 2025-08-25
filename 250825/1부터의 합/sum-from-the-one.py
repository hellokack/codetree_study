num=int(input())
cnt=0
for i in range(100):
    cnt += i
    if cnt >=num:
        print(i)
        break