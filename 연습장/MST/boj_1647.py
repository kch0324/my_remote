# 도시 분할 계획
# 전체 마을의 mst를 구한 뒤 가중치가 가장 높은 간선을 제거
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
for i in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
edges.sort()
parent = [i for i in range(N + 1)]
def find_set(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union_set(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry:
        return False
    else:
        parent[rx] = ry
        return True

total = 0
max_w = 0
for w, u, v in edges:
    if union_set(u, v):
        total += w
        max_w = max(max_w, w)

print(total - max_w)