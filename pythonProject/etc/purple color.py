T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 영역의 개수
    arr = [[0] * 10 for _ in range(10)]     # 빈 10 * 10 2차원 리스트
    # 영역을 생성하는 회수만큼 반복하며 영역의 color로 빈 리스트를 색칠
    for state in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if arr[r][c] == color:      # 이미 같은 색이 색칠되어 있다면 건너뛰기
                    continue
                else:
                    arr[r][c] += color      # 아니라면 해당 색을 추가

    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:      # 보라색이 색칠되어 있는 칸이라면 카운트 +1
                cnt += 1
    print(f"#{tc} {cnt}")













