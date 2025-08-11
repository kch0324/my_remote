T = int(input())
for tc in range(1, T + 1):
    i, j, N = map(int, input().split())
    arr = [[0] * 10 for _ in range(10)]
    number = 1
    for r in range(i, i + N):
        for c in range(j, j + N):
            arr[r][c] = number
            number +=1
    print(f"#{tc}")
    for a in range(10):
        print(' '.join(map(str, arr[a])))