# 최소 스패닝 트리
# Prim 연습
from heapq import heappop, heappush
V, E = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(E)]

graph = {}
dist = [float('inf')] * (V + 1)  # 최적화용 메모
dist[1] = 0     # 시작점 초기화

for u, v, w in arr:
    graph.setdefault(u, []).append([v, w])
    graph.setdefault(v, []).append([u, w])

def prim(start):
    pq = [start]
    visited = set()
    min_w = 0
    while pq:
        w, u = heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        min_w += w

        for v, w in graph[u]:
            if v in visited or dist[v] <= w:
                continue
            dist[v] = w
            heappush(pq, (w, v))
    return min_w

result = prim((0, 1))
print(result)