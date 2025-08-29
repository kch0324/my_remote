# 중위 순회로 하면 1 ~ N 트리 삽입 가능

T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # N: 노드의 개수

    left = [0] * (N + 1)
    right = [0] * (N + 1)
    val = [0] * (N + 1)
    for i in range(1, N + 1):
        if i*2 <= N:
            left[i] = i*2
        if i*2 + 1 <= N:
            right[i] = i*2 +1

    i = 1
    def make_tree(v):   # 중위 순회
        global i
        if v == 0:
            return
        while v:   # 자식이 없을때까지 내려가고 제일 아래부터 순서대로 삽입
            make_tree(left[v])
            val[v] = i
            i += 1
            make_tree(right[v])
            return

    make_tree(1)
    print(f"#{tc} {val[1]} {val[N // 2]}")