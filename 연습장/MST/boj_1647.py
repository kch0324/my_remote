# 도시 분할 계획
# 전체 마을의 mst를 구한 뒤 가중치가 가장 높은 간선을 제거
# Prim 쓰고 싶으니까 그냥 mst선택할때 가중치 제일 높은 간선을 저장해두자
from heapq import heappush, heappop 
N, M = map(int, input().split())
graph = {}
for i in range(M):
    u, v, w = map(int, input().split())
    graph.setdefault(u, []).append((w, v))
    graph.setdefault(v, []).append((w, u))

INF = float('inf')
dist = [INF] * (N + 1)

def prim(start):
    pq = [start]
    visited = set()
    total = 0
    max_v = 0   # 간선은 양수이므로 가장 큰 가중치 초기값 0
    while pq:
        w, u = heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        total += w
        max_v = max(max_v, w)
        
        for nw, v in graph[u]:
            if v in visited or dist[v] <= nw:
                continue
            dist[v] = nw
            heappush(pq, (nw, v))
    return total - max_v

result = prim((0, 1))
print(result)