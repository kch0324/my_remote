T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    a = 0
    b = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    snail[0][0] = 1

    for t in range((2*N-1) // 4 + 1):
        for p in range(4):
            for q in range(1, N + 1):
                di = a + dr[p] * q
                dj = b + dc[p] * q
                if 0<= di < N and 0 <= dj < N:      # 범위를 넘어가지 않을때
                    if snail[di][dj] == 0:      # 해당 칸이 채워지지 않았으면
                        snail[di][dj] = snail[di - dr[p]][dj - dc[p]] + 1   # 전 배열의 +1만큼 다음 배열에 할당
                    else:
                        a = di - dr[p]      # 이미 채워져있으면 좌표저장후 방향전환
                        b = dj - dc[p]
                        break
                else:
                    a = di - dr[p]      # 범위를 넘어가도 좌표저장후 방향전환
                    b = dj - dc[p]
                    break

    print(f"#{tc}")
    for i in snail:
        print(' '.join(map(str, i)))