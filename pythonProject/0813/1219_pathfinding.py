def dfs_stack(start, goal):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node == goal:
            return 1

        elif node not in visited:
            visited.add(node)
            # 중요!! 그래프의 노드가 전부 만들어진게 아니라 필요한 것만 만들었으므로 있을때만 불러옴
            if node in graph.keys():
                stack.extend(graph[node])
    return 0


for t in range(1, 11):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = {}
    for i in range(N * 2):  # 짝수번만 두 수를 u, v에 저장하여 중복방지 두번중 한번만 저장하므로 간선 * 2만큼
        if i % 2 == 0:
            u, v = arr[i], arr[i+1]
            graph.setdefault(u, []).append(v)   # 유향 간선으로 그래프에 추가
        else:
            continue

    print(f"#{tc} {dfs_stack(1, 99)}")