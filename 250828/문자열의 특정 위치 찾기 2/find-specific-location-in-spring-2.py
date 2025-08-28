alpha=input()
cnt=0
list=["apple","banana","grape","blueberry","orange"]
for i in list:
    if i[2]==alpha or i[3]==alpha:
        cnt+=1
        print(i)
print(cnt)