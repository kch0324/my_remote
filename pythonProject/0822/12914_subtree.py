T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())    # E: 간선개수, N: 루트
    arr = list(map(int, input().split()))
    # 트리 유향 간선 구현
    tree = {}
    for i in range(0, E*2, 2):
        u, v = arr[i], arr[i+1]
        tree.setdefault(u, []).append(v)

    cnt = 0
    # 자식 노드에 접근할때 cnt + 1 해주는 함수 구현
    def get_sub(v):
        global cnt
        cnt += 1
        if v not in tree:
            return
        for n in tree[v]:
            get_sub(n)
    
    get_sub(N)

    print(F"#{tc} {cnt}")