num=0
while True:
    num=int(input())
    if num==25:
        print("Good")
        break
    if num<25:
        print("Higher")
    else:
        print("Lower")