from collections import deque
def BFS(s, g, N):
    Q = deque()
    Q.append(s)
    visited = [0] * (N + 1)
    while Q:
        k = Q.popleft()
        for i in graph[k]:
            if visited[i] == 0:
                Q.append(i)
                visited[i] = visited[k] + 1
    return visited[g]

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = {}
    for i in range(E):
        u, v = map(int, input().split())
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    S, G = map(int, input().split())

    result = BFS(S, G, V)
    print(f"#{tc} {result}")