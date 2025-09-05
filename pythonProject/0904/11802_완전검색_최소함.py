# (0,0)에서 (n-1,n-1)까지 가야한다.
# 오른쪽이나 아래로만 이동 가능 -> (x + 1) or (y + 1) 보기쉽게 간선할당
# DFS 재귀로 최솟값 갱신해서 출력
from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N =  int(input())   # N: 배열의 행,열 길이
    arr = [list(map(int, input().split())) for _ in range(N)]   # arr: NxN 크기의 숫자배열

    graph = {}
    # 정점의 좌표로 그래프 구현 (오른쪽, 아래쪽 간선 할당)
    for i in range(N):
        for j in range(N):
            u, v = (i, j), []
            Ni, Nj = i + 1, j + 1
            if 0 <= Ni < N:  # 아래쪽 인접 정점
                v.append((Ni, j))
            if 0 <= Nj < N:  # 오른쪽 인접 정점
                v.append((i, Nj))
            graph[u] = v

    # DFS로 최솟값 탐색
    min_v = float('inf')
    node_min_total = [[float('inf')] * N for _ in range(N)]  # 각 중간 노드들의 현재합의 최솟값 리스트
    def DFS(start):  # 매개변수의 인자로 (좌표튜플, 현재합)을 받음
        global min_v, node_min_total
        stack = deque([start])
        while stack:
            node, total = stack.pop()   # 정점의 좌표와 현재합을 언패킹해서 사용
            # 같은 노드에 도착했을때 현재합이 해당노드 최소 현재합이었던 것 보다 높으면 가지치기
            if total >= node_min_total[node[0]][node[1]]:
                continue
            else:
                node_min_total[node[0]][node[1]] = total
            if node == (N-1, N-1):   # 끝까지 도착했으면 최솟값 갱신
                min_v = min(min_v, total)
                continue
            for next_node in graph[node]:   # 인접한 정점들(오른쪽, 아래)를 for문으로 돌려서 스택에 push
                ni, nj = next_node[0], next_node[1]
                stack.append((next_node, total + arr[ni][nj]))

    DFS(((0,0), arr[0][0]))
    print(f"#{tc} {min_v}")