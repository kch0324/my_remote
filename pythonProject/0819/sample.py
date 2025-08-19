def min_sum(i, n, s):    # i번째원소, n 집합의 크기, s i-1 까지의 원소들의 합
    global min_v
    arr[0][]
    if s >= min_v:  # 최솟값보다 s가 커지면 탈출
        return
    elif i == n:    # n까지 도달했을때
        if s < min_v:   # s가 최솟값보다 작으면 갱신
            min_v = s
        else:
            return

    else:
        for j in range(i, n):
            bit[i], bit[j] = bit[j], bit[i]
            min_sum(i+1, n, s + arr[i])
            bit[i], bit[j] = bit[j], bit[i]




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bit = [0, 1, 2]
    min_v = float('inf')
