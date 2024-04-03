t = int(input("Enter number of test cases: "))
result = []
for _ in range(t):
    n = int(input("Enter number of task: "))
    graphic = []
    for _ in range(n):
        graphic.append(list(map(int, input().split())))
    graphic.sort(key=lambda x: x[1])
    parent = {'C': 0, 'J': 0}
    current_symbol = 'C'
    current_result = ""

    for i in range(0, n):
        if parent['C'] <= graphic[i][0]:
            current_result += 'C'
            parent['C'] = graphic[i][1]
        elif parent['J'] <= graphic[i][0]:
            current_result += 'J'
            parent['J'] = graphic[i][1]
        else:
            current_result = 'IMPOSSIBLE'
            break

    result.append(current_result)

for i in range(t):
    print(f"Case #{i + 1}: {result[i]}")
