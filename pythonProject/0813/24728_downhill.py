
# 5. max_v 변수를 선언하고 temp와 비교해서 최댓값 갱신

# 1. dfs_stack 함수를 만듬
def dfs_stack(graph, start):
    stack = [start]
    visited = set()
    cnt = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            cnt += 1
            # 중요!! 그래프의 노드가 전부 만들어진게 아니라 필요한 것만 만들었으므로 있을때만 불러옴
            if node in graph.keys():
                stack.extend(graph[node])
    return cnt

Dr = [0, 0, -1, 1]
Dc = [1, -1, 0, 0]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    graph = {}

    # 2. NxN 배열을 행우선 순회하면서 상하좌우 델타값으로 주변에 접근
    for i in range(N):
        for j in range(N):
            center = arr[i][j]
            min_v = 501
            # 3. 해당 arr[i][j] 값과 상하좌우 arr값을 비교해서 중심보다 주변의 min_v가 더 낮다면 graph에 유향 간선 추가
            for p in range(4):
                Di = i + Dr[p]
                Dj = j + Dc[p]
                if 0 <= Di < N and 0 <= Dj < N:
                    temp = arr[Di][Dj]
                    min_v = min(min_v, temp)
            if center > min_v:
                u, v = center, min_v
                graph.setdefault(u, []).append(v)
    # 4. NxN 배열을 열순회 하며 dfs_stack 함수를 호출해서 이동거리 temp 반환
    max_v = 0
    for i in range(N):
        for j in range(N):
            start = arr[i][j]
            temp = dfs_stack(graph, start)
            max_v = max(max_v, temp)

    print(f"#{tc} {max_v}")