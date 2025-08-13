def dfs_stack(start, goal):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node == goal:
            return 1
        elif node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = {i: [] for i in range(1, V+1)}
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
    S, G = map(int, input().split())

    print(f"#{tc} {dfs_stack(S, G)}")