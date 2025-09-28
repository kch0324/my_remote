# 네트워크 연결
# Prim 연습, 최적화 버전
from heapq import heappush, heappop
N = int(input())    # 정점 수
M = int(input())    # 간선 수

graph = {}
for i in range(M):
    u, v, w = map(int, input().split())
    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))

dist = [float('inf')] * (N + 1)
def prim(start):
    pq = [start]
    visited = set()  # visited: 선택한 mst
    total = 0   # 최소비용
    while pq:
        w, u = heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        total += w  # 선택한 가중치를 더함
        
        for v, w in graph[u]:
            if v in visited or dist[v] <= w:
                continue
            dist[v] = w
            heappush(pq, (w, v))
    return total

result = prim((0, 1))
print(result)