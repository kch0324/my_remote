# 상하좌우 델타로 주변 좌표 접근 -> 0이면 진행
# 길이 막히면 stack 을 pop해서 갈림길로 돌아감
def backtracking(start, goal):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node == goal:
            return 1
        elif node not in visited:   # 방문기록 저장후 인접 node를 stack에 push
            visited.add(node)
            stack.extend(graph[node])
    return 0

T = int(input())
Dr = [0, 0, -1, 1]
Dc = [-1, 1, 0, 0]
for tc in range(1, T + 1):
    N = int(input())    # NxN 크기의 미로
    graph = {(i, j): [] for i in range(N) for j in range(N)}    # (i,j) 좌표를 정점으로 빈 그래프 생성
    arr = [list(map(int, input())) for _ in range(N)]    # 2차원 그래프에 input 받음
    # 상하좌우 델타로 각 정점들의 간선에 접근
    for i in range(N):
        for j in range(N):
            # 2와 3의 값을 가진 좌표를 찾으면 s, g에 할당
            if arr[i][j] == 2:
                s = (i, j)
            elif arr[i][j] == 3:
                g = (i, j)
            for p in range(4):
                Di = i + Dr[p]
                Dj = j + Dc[p]
                if 0 <= Di < N and 0 <= Dj < N:     # 델타값의 범위 제한
                    if arr[Di][Dj] == 0:
                        u, v = (i, j), (Di, Dj)     # 좌표를 정점으로 인접 정점들 그래프에 무형 간선 할당
                        graph[u].append(v)
                        graph[v].append(u)
                else:
                    continue

    print(f"#{tc} {backtracking(s, g)}")