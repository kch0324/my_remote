from collections import deque

def BFS(s, g):
    visited = [[-1] * N for _ in range(N)]  # visited를 2차원 빈 리스트(-1)로 설정
    Q = deque()
    Q.append(s)
    while Q:
        k = Q.popleft() # Q 안에 있는 것은 정점의 좌표 튜플
        for i in graph[k]:  # 해당 정점에 인접한 정점들을 돌면서 visited의 해당 좌표에 거리값을 더해줌
            if visited[i[0]][i[1]] == -1:
                Q.append(i)
                visited[i[0]][i[1]] = visited[k[0]][k[1]] + 1
    return visited[g[0]][g[1]]  # 목표지점의 거리값 반환



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]    # NxN 배열
    graph = {}  # 빈 그래프
    Dr = [0, 0, 1, -1]; Dc = [1, -1, 0, 0]  # 4방향 델타

    # 행우선 순회로 인접한 정점들이 둘다 1이 아니면 양방향 간선 그래프에 할당
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                continue
            if arr[i][j] == 2:
                start = (i, j)
            if arr[i][j] == 3:
                goal = (i, j)
            for p in range(4):
                Ni = i + Dr[p]; Nj = j + Dc[p]
                # 인접 상하좌우 정점이 배열범위를 초과하지 않고 1이 아니라면 간선 할당
                if 0 <= Ni < N and 0 <= Nj < N and arr[i][j] != 1 and arr[Ni][Nj] != 1:
                    graph.setdefault((i, j), []).append((Ni, Nj))
                    graph.setdefault((Ni, Nj), []).append((i, j))

    result = BFS(start, goal)
    if result == -1:
        result = 0

    print(f"#{tc} {result}")