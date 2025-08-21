from collections import deque


def bfs_max_d(start):
    Q = deque()
    Q.append(start)
    visited = [0] * 101  # 번호는 1이상 100이하
    while Q:
        k = Q.popleft()
        if k not in graph:  # 노드가 모두 연결된 건 아니므로 그래프에 없는 키가 나오면 건너뜀
            continue
        for i in graph[k]:
            if visited[i] == 0:  # visited i인덱스가 비어있으면
                Q.append(i)
                visited[i] = visited[k] + 1
    # visited 에서 거리가 가장 높은 인덱스 최댓값 갱신
    max_d = visited[start]
    max_idx = start
    for j in range(101):
        if max_d <= visited[j]:
            max_d = visited[j]
            max_idx = j
    return max_idx


for tc in range(1, 11):
    N, start = map(int, input().split())  # N: 노드 쌍 길이, start: 시작노드
    arr = list(map(int, input().split()))
    graph = {}
    # arr인덱스가 짝수번일때만 그래프에 유향 간선 할당
    for item in range(N):
        if item % 2 == 0:
            u, v = arr[item], arr[item + 1]
            graph.setdefault(u, []).append(v)

    print(f"#{tc} {bfs_max_d(start)}")