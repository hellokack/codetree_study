num=int(input())
cnt=0
for i in range(101):
    cnt += i
    if cnt >=num:
        print(i)
        break