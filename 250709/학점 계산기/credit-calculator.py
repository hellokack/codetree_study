sub=int(input())
grade = list(map(float, input().split()))

hap=0
for i in grade:
    hap += i
avg = hap/sub
print(f"{avg:.1f}")
if avg>=4.0:
    print("Perfect")
elif avg>=3.0:
    print("Good")
else:
    print("Poor")