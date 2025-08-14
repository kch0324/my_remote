T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N = 보드길이, M = 턴 횟수
    # NxN 보드 빈칸이면 0 , 흑돌 1 , 백돌 2 / 가운데 4칸 흑,백 -> (N / 2), (N / 2 + 1) 좌표 -1 씩
    board = [[0] * N for _ in range(N)]
    dx = (N // 2 - 1, N // 2)     # 초기 중앙값 4개를 위한 델타
    board[dx[0]][dx[0]] = 2
    board[dx[0]][dx[1]] = 1
    board[dx[1]][dx[0]] = 1
    board[dx[1]][dx[1]] = 2

    dr = [0, 0, 1, -1, 1, 1, -1, -1]
    dc = [1, -1, 0, 0, 1, -1, -1, 1]
    for t in range(M):
        x, y, c = map(int, input().split())   # c(color)
        # 인풋이 1이상부터 주어지므로 각각 -1 씩
        x -= 1 ; y -= 1
        board[y][x] = c   # 보드에 해당 좌표에 돌을 놓음
        # 8방향 델타 배열로 기준 좌표부터 같은 색 돌을 만날때까지 사이 돌들 색 바꾸기
        for p in range(8):
            di, dj = y, x
            inner = []
            while True:
                di += dr[p]
                dj += dc[p]
                if 0 <= di < N and 0 <= dj < N:   # 범위 체크
                    if board[di][dj] == 0:   # 인접 돌이 없는 경우 break
                        break
                    elif board[di][dj] != c:  # 다른 색 돌을 만난 경우 inner 에 좌표를 저장
                        inner.append([di, dj])
                    else:   # 같은 색 돌을 만난 경우 그동안 저장한 inner의 돌들의 색을 바꾸고 종료
                        for i in range(len(inner)):
                            a, b = inner[i][0], inner[i][1]
                            board[a][b] = c
                        break
                else:    # 범위 벗어나면 break
                    break
    # 행우선 순회로 흑/백 돌 카운트
    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print(f"#{tc} {black} {white}")