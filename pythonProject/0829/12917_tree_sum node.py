def get_pal(num):   # LRV 후위순회로 리프노드부터 값을 num까지 더해서 가져옴
    if num == 0:
        return 0
    l = get_pal(left[num])
    r = get_pal(right[num])
    return l + r + val[num]

T = int(input())
for tc in range(1, T +1):
    N, M, L = map(int, input().split())     # N: 노드 개수, M: 리프노드 개수, L: 타겟 노드 번호
    left = [0] * (N+1)
    right = [0] * (N+1)
    val = [0] * (N+1)

    for i in range(1, N+1):     # 좌우 자식 노드들 간선 할당해줌
        if i*2 <= N:
            left[i] = i*2
        if i*2 + 1 <= N:
            right[i] = i*2 + 1

    for _ in range(M):  # 리프노드들 키를 인덱스로 값을 val리스트에 넣어줌
        num, v = map(int, input().split())
        val[num] = v

    print(f"#{tc} {get_pal(L)}")