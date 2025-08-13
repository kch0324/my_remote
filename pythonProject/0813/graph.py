for _ in range(M):             # M번 반복 (간선 개수만큼)
    u, v = map(int, input().split())   # 간선의 시작점 u, 끝점 v 입력
    graph[u].append(v)         # u → v 방향 연결 추가
    graph[v].append(u)         # v → u 방향 연결 추가 (무방향일 경우)


# 그래프(인접 리스트 형태)
graph = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3]
}

# DFS (스택 사용)
def dfs_stack(start):
    visited = set()      # 방문한 노드를 기록
    stack = [start]      # 시작 노드를 스택에 넣음

    while stack:         # 스택이 빌 때까지 반복
        node = stack.pop()  # 스택에서 꺼내기 (LIFO 구조)
        if node not in visited:
            visited.add(node)           # 방문 처리
            print(node, end=' ')        # 현재 노드 출력
            # 인접 노드를 역순으로 넣어 방문 순서 맞추기
            stack.extend(reversed(graph[node]))