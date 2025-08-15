T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    space = [list(map(int, input().split())) for _ in range(N)]
 
    count = 0
    dr = [0, 1, 0, -1] 
    dc = [1, 0, -1, 0]
 
    for i in range(N):
        for j in range(N):
            if space[i][j] == 2:  # 몬스터 위치
                for d in range(4):  # 4방향
                    for m in range(1, N):  # 최대 N칸까지 레이저
                        ni = i + dr[d] * m
                        nj = j + dc[d] * m
 
                        if 0 <= ni < N and 0 <= nj < N:
                            if space[ni][nj] == 0:
                                space[ni][nj] = 1
                            else:
                                break  # 0이 아니면 레이저 멈춤
                        else:
                            break  # 범위 밖이면 레이저 멈춤
 
    for i in range(N):
        for j in range(N):
            if space[i][j] == 0:
                count += 1
 
    print(f"#{tc} {count}")
##########################################################################################################################
