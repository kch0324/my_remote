# 각 관리구역을 모두 방문하고 마지막에 사무실로 복귀

T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # N: 지점 개수
    arr = [list(map(int, input().split())) for _ in range(N)]   # arr: i와 j간의 거리가 담긴 2차원 배열

    min_v = float('inf')
    visited = [0] * N

    def recur(start, depth, total):
        global min_v
        if total >= min_v:  # 거리 합이 이미 최솟값을 넘어가면 가지치기
            return
        if depth == N - 1:  # 마지막 지점에 도달하면 출발점으로 가는 거리를 더해주고 최솟값 갱신
            min_v = min(min_v, total + arr[start][0])
            return
        for goal in range(1, N):   # 모든 지점 루프 (출발지 제외)
            if visited[goal]:   # 방문한 지점은 건너뛰기
                continue
            visited[goal] = 1
            recur(goal, depth + 1, total + arr[start][goal])   # 도착지를 출발지로 바꾸고, 재귀횟수 + 1, 거리합을 갱신한 걸 다음 함수로 넘겨줌
            visited[goal] = 0

    recur(0, 0, 0)
    print(f"#{tc} {min_v}")