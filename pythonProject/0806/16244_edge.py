T = int(input())
for tc in range(1, T + 1):
    i, j, N = map(int, input().split())
    arr = [[0] * 10 for _ in range(10)]
    for r in range(i, i + N):
        for c in range(j, j + N):
            arr[r][c] = 1
    for p in range(i + 1, i + N - 1):
        for q in range(j + 1, j + N - 1):
            arr[p][q] = 0
    print(f"#{tc}")
    for a in range(10):
        print(' '.join(map(str, arr[a])))