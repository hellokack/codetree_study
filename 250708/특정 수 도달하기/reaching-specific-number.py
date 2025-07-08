num = input().split()
num2=[]
hap=0
for i in num:
    while int(i) >= 250:
        num2.append(i)
    hap += int(i)
avg_num= hap / len(num)
print(hap,'',avg_num)

