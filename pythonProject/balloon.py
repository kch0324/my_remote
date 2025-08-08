T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]     # 꽃가루가 들어있는 전체 영역 생성
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    max_flower = arr[1][1] + arr[0][1] + arr[1][0] + arr[1][2] + arr[2][1]      # 꽃가루가 제일 많은 범위의 초기값

    for i in range(N):      # i, j는 중앙 풍선의 좌표
        for j in range(M):
            temp_flower = arr[i][j]     # 중앙 풍선의 꽃가루 +
            for p in range(4):      # 중앙 풍선으로부터 각 네방향으로 범위만큼 이동한 풍선
                di = i + dr[p]
                dj = j + dc[p]
                if 0 <= di < N and 0 <= dj < M:     # 인덱스 범위를 넘어가지 않기 하게 위한 if문
                    temp_flower += arr[di][dj]      # 해당 풍선의 꽃가루 +

            if max_flower < temp_flower:
                max_flower = temp_flower

    print(f"#{tc} {max_flower}")