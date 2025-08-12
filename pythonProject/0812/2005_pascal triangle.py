T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * p for p in range(1, N+1)]
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                result = 0
                if 0 <= j-1:
                    result += arr[i-1][j-1]
                if j < i:
                    result += arr[i-1][j]

                arr[i][j] = result
    print(f"#{tc}")
    for p in range(N):
        print(*arr[p])
