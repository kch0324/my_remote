def subsets(i, n, s, k):  # i원소, n 부분집합의 크기, s i-1까지 고려된 합, k 원소합
    global cnt

    if s > k:   # 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    elif sum(bit) > n:  # 부분집합의 크기가 n을 넘을 경우
        return
    else:
        if sum(bit) == n:
            if s == k:    # 부분집합의 크기가 n이고 원소의 합이 k가 되면
                cnt += 1
                return
            else:    # 부분집합의 크기는 n이지만 원소의 합이 k가 아니면
                return
        elif i == 12:   # 부분집합의 크기가 아직 n보다 작을 때 끝까지 간 경우
            return
        else:   # 부분집합의 크기가 n보다 작고, 끝까지 아직 가지 않은 경우
            bit[i] = 1
            subsets(i+1, n, s+arr[i], k)    # arr[i] 포함
            bit[i] = 0
            subsets(i+1, n, s, k)         # arr[i] 미포함

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # N개의 원소, 원소들의 합 K
    arr = [i for i in range(1, 13)]  # arr = [1, 2, 3, ... 10, 11, 12]
    bit = [0] * 12
    cnt = 0

    subsets(0, N, 0, K)
    print(f"#{tc} {cnt}")