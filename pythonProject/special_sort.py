T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    for i in range(N):
        max_idx = i
        min_idx = i
        idx = i
        for j in range(i+1, N):
            if i % 2 == 0:
                if ai[max_idx] < ai[j]:
                    max_idx = j
                    idx = j
            else:
                if ai[min_idx] > ai[j]:
                    min_idx = j
                    idx = j

        ai[i], ai[idx] = ai[idx], ai[i]

    bi = [0] * 10
    for j in range(10):
        bi[j] = ai[j]

    print(f"#{tc} {' '.join(map(str, bi))}")