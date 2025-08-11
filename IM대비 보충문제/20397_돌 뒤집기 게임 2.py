T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for c in range(M):
        i, j = map(int, input().split())
        for turn in range(1, j + 1):
            if i-1 - turn >= 0 and i-1 + turn < N: 
                if arr[i-1 - turn] == arr[i-1 + turn]:
                    if arr[i-1 + turn] == 0:
                        arr[i-1 - turn] = arr[i-1 + turn] = 1
                    else:
                        arr[i-1 - turn] = arr[i-1 + turn] = 0
    print(f"#{tc} {' '.join(map(str, arr))}")