import copy
def get_min(arr, i, N, M, K, ch):
    global min_v, cnt
    if i == N:  # 끝까지 돌경우 종료
        return
    if min_v <= cnt:    # 가지치기 종료
        return
    for c in range(M):  # 열우선 순회 중첩 탐색
        stack = [arr[0][c]]
        for r in range(1, N):
            if len(stack) == K:     # 열에 K개이상 중첩되면 break 
                break
            node = stack.pop()
            if node == arr[r][c]:
                stack.append(node)
                stack.append(arr[r][c])
            else:
                stack.clear()
                stack.append(arr[r][c])
        if len(stack) != K:     # 끝까지 돌았는데 열에 K개만큼 중첩이 없으면 탐색중지
            break
    else:   # 모든 열에 K개 중첩을 찾으면 min_v 갱신 후 종료
        min_v = min(min_v, cnt)
        return

    for j in range(M):  # 약품 투입
        arr[i][j] = ch
    cnt += 1
    get_min(arr, i + 1, N, M, K, 1)
    get_min(arr, i + 1, N, M, K, 0)

T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())    # D: 두께(N), W: 가로크기(M), K: 합격기준
    arr = [list(map(int, input().split())) for _ in range(D)]
    arr2 = copy.deepcopy(arr)
    min_v = float('inf')
    cnt = 0
    get_min(arr, 0, D, W, K, 1)
    cnt = 0
    get_min(arr2, 0, D, W, K, 0)
    print(f"#{tc} {min_v}")