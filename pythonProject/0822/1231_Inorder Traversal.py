# 중위 순회: LVR
# 완전이진트리: lv[i] = i*2, rv[i] = i*2 + 1
for tc in range(1, 11):
    N = int(input())    # N: 정점 수
    arr = [list(input().split()) for _ in range(N)]
    arr = [0] + arr     # 인덱스 번호 1부터 맞춰서 arr 생성

    # 왼쪽, 오른쪽 자식노드 간선번호와 번호에 들어갈 값 리스트 생성
    lv = [0] * (N + 1)
    rv = [0] * (N + 1)
    val = [0] * (N + 1)

    # lv, rv, val 리스트 구현
    for i in range(1, N + 1):
        val[i] = arr[i][1]
        if i*2 <= N:
            lv[i] = i*2
        if i*2 + 1 <= N:
            rv[i] = i*2 + 1

    # 트리를 중위순회로 탐색하는 함수 생성
    def get_in_order(v):
        if v == 0:
            return
        get_in_order(lv[v])
        result.append(val[v])
        get_in_order(rv[v])

    result = []
    get_in_order(1)
    print(f"#{tc} {''.join(result)}")