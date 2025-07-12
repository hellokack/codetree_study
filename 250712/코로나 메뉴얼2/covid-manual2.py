num=[0,0,0]
for i in range(3):
    num[i] =list(input().split())
emerg=[0]*4
for i in num:
    if i[0] == "Y":
        if int(i[1]) >=37:
            emerg[0] +=1
        else:
            emerg[2] +=1
    else:
        if int(i[1]) >=37:
            emerg[1] +=1
        else:
            emerg[3] +=1
if emerg[0] >=2:
    emerg.append('E')
for i in emerg:
    print(i, end=' ')
