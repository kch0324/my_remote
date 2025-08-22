# 한번 탐색할때 cnt += 1
# N/2번째 탐색의 안에 든 값: cnt == N//2 이 될때 result에 cnt저장, 루트안에 든 값도 마찬가지

T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # N: 노드의 개수

    lv = [0] * (N + 1)
    rv = [0] * (N + 1)
    for i in range(1, N + 1):
        if i*2 <= N:
            lv[i] = i*2
        if i*2 + 1 <= N:
            rv[i] = i*2 +1

    cnt = 0
    def get_num(v):
        global cnt
        if v == 0:
            return
        get_num(lv[v])
        cnt += 1
        get_num(rv[v])

    get_num(1)
    result1 = cnt
    cnt = 0
    get_num(N//2)
    result2 = cnt
    print(f"#{tc} {result1} {result2}")