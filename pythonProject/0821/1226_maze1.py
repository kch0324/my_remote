from collections import deque
def BFS(start, goal):
    Q = deque()
    visited = set()
    Q.append(start)
    while Q:
        if goal in visited: # goal에 접근하면 리턴 1
            return 1
        k = Q.popleft()
        for t in graph[k]:
            if t not in visited:
                visited.add(t)
                Q.append(t)
    return 0    # 아니면 리턴 0

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]  # 16x16 행렬
    Dx = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    graph = {}
    # 행우선 순회로 중심좌표가 1이 아니면 상하좌우 델타가 1이 아닐때 양방향 간선 그래프 할당
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 1: continue
            if arr[i][j] == 2: start = (i, j)
            if arr[i][j] == 3: goal = (i, j)
            for Dr, Dc in Dx:
                Di, Dj = i + Dr, j + Dc
                if 0 <= Di < 16 and 0 <= Dj < 16 and arr[Di][Dj] != 1:
                    u, v = (i, j), (Di, Dj)
                    graph.setdefault(u, []).append(v)
                    graph.setdefault(v, []).append(u)

    print(f"#{tc} {BFS(start, goal)}")