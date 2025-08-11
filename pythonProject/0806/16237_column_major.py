T = int(input())
for tc in range(1, T + 1):
    i, j, N, M = map(int, input().split())
    arr = [[0] * 10 for _ in range(10)]
    number = 1
    for c in range(j, j + N):
        for r in range(i, i + M):
            arr[r][c] = number
            number += 1
    print(f"#{tc}")
    for a in range(10):
        print(' '.join(map(str, arr[a])))