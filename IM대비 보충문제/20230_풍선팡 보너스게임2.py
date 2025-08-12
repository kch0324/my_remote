T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # 격자 크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    Dr = [0, 0, 1, -1]
    Dc = [1, -1, 0, 0]
    max_v = 0

    for i in range(N):
        for j in range(N):
            temp_v = arr[i][j]
            for p in range(1, N):
                for k in range(4):
                    Di = i + Dr[k] * p
                    Dj = j + Dc[k] * p
                    if 0 <= Di < N and 0 <= Dj < N:
                        temp_v += arr[Di][Dj]
            max_v = max(max_v, temp_v)
    print(f"#{tc} {max_v}")