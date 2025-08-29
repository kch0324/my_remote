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


# E, N = map(int, input().split())
# arr = list(map(int, input().split()))
# V = E + 1
# left = [0] * (V + 1)
# right = [0] * (V + 1)

# for i in range(E):
#     p, c = arr[i*2], arr[i*2+1]
#     if left[p] == 0:
#         left[p] = c
#     else:
#         right[p] = c


# def pre_order(T):   # 전위순회, 방문한 정점(부모) 먼저 처리
#     if T == 0:   # 0이 아니면 (존재하는 정점이면)
#         return 0
#     l = pre_order(left[T])  # 왼쪽 자식(서브트리)로 이동
#     r = pre_order(right[T]) # 오른쪽 자식(서브트리)로 이동
#     return l + r + 1

# print(pre_order(N))