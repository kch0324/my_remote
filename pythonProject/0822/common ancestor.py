T = int(input())
for tc in range(1, T + 1):
    V, E, v1, v2 = map(int, input().split())
    arr = list(map(int, input().split()))
    child = [[] for _ in range(V + 1)]  # 인덱스: 부모 노드 / 값: 자식 노드들(2개씩)
    pal = [0] * (V + 1)     # 인덱스: 자식 노드 / 값: 부모 노드
    for i in range(E):
        u, v = arr[i*2], arr[i*2+1]
        child[u].append(v)
        pal[v] = u

    def get_anc(v):
        anc = []
        if v == 0:  # 부모가 없으면
            return
        while v > 1:
            anc.append(pal[v])
            v = pal[v]
        return anc

    anc1, anc2 = get_anc(v1), get_anc(v2)

    for a1 in anc1:
        for a2 in anc2:




