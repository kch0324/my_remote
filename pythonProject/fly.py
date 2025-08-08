T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]     # 파리가 들어있는 전체 영역 생성
    max_fly = arr[0][0] + arr[0][1] + arr[1][0] + arr[1][1]      # 파리가 제일 많은 범위의 초기값

    for i in range(N - M + 1):      # i, j는 파리채의 왼쪽위 모서리값
        for j in range(N - M + 1):
            temp_fly = 0
            for p in range(M):      # p, q는 파리채의 왼쪽위 모서리부터 M범위만큼 움직인 범위
                for q in range(M):
                    temp_fly += arr[i+p][j+q]
            if max_fly < temp_fly:
                max_fly = temp_fly

    print(f"#{tc} {max_fly}")
