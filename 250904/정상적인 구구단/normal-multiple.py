num = int(input())
for i in range(1, num + 1):
    for j in range(1, num + 1):
        # j가 num과 같으면 (즉, 줄의 마지막이면) 쉼표 없이 출력
        if j == num:
            print(f"{i} * {j} = {i*j}")
        # 그 외의 경우에는 쉼표와 함께 출력
        else:
            print(f"{i} * {j} = {i*j}", end=", ")