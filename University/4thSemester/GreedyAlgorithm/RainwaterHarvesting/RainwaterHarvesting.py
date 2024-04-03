t = int(input("Enter number of test cases: "))
for _ in range(t):
    n = int(input("Enter size of array: "))
    print("Enter number of elements:")
    arr = list(map(int, input().split()))

    total_water = 0
    for i in range(1, n - 1):
        left = arr[i]
        right = arr[i]

        for j in range(i):
            left = max(arr[j], left)

        for j in range(i + 1, n):
            right = max(right, arr[j])

        total_water += (min(left, right) - arr[i])

    print(total_water)

