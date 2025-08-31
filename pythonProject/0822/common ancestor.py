def get_anc(v): # 1. [조상 리스트를 반환하는 함수]
    anc = []
    if v == 0:  # 부모가 없으면
        return
    while v > 1:    # 부모들을 v부터 가까운 순서대로 리스트에 담아 반환
        anc.append(pal[v])
        v = pal[v]
    return anc

def get_common(anc1, anc2): # 2. [가장 가까운 공통 조상을 반환하는 함수]
    for a1 in anc1:
        for a2 in anc2:
            if a1 == a2:
                return a1
            
def DFS(start): # 3. [DFS로 하위 정점 개수를 반환하는 함수]
    stack = [start]
    visited = set()
    cnt = 0
    while stack:
        node = stack.pop()
        cnt += 1
        if node not in visited:
            visited.add(node)
            stack.extend(child[node])
    return cnt

T = int(input())
for tc in range(1, T + 1):
    V, E, v1, v2 = map(int, input().split())
    arr = list(map(int, input().split()))
    child = [[] for _ in range(V + 1)]  # 인덱스: 부모 노드 / 값: 자식 노드들(2개씩)
    pal = [0] * (V + 1)     # 인덱스: 자식 노드 / 값: 부모 노드
    # 트리 간선 구현 (자식, 부모 간선)
    for i in range(E):
        u, v = arr[i*2], arr[i*2+1]
        child[u].append(v)
        pal[v] = u

    anc1, anc2 = get_anc(v1), get_anc(v2) 
    common = get_common(anc1, anc2)

    print(f"#{tc} {common} {DFS(common)}")