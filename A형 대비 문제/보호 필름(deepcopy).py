from copy import deepcopy
# i: 행(재귀횟수), D: D까지 재귀(두께), W: 가로크기, K: 합격기준, arr: 배열, cnt: 약품 투입횟수
def DFS(i, D, W, K, arr, cnt):
    global min_v
    if cnt >= min_v:  # 최소값보다 시행횟수 많아지면 탈출
        return
    if check(arr, D, W, K):  # 합격기준 달성했는지 확인후 최소 시행횟수 갱신
        min_v = min(min_v, cnt)
        return
    if i >= D:  # 끝까지 가면 탈출
        return
    copy_arr = deepcopy(arr)  # 1. 약품 투입 안하고 다음 층 넘어가는 경우
    DFS(i + 1, D, W, K, copy_arr, cnt)

    for p in range(2):  # 2. 약품 투입 하는 경우 (0일때 / 1일때)
        copy_arr[i] = [p] * W
        DFS(i + 1, D, W, K, copy_arr, cnt + 1)


def check(arr, D, W, K):
    if K <= 1:
        return True

    for c in range(W):
        stack = 1
        prev = arr[0][c]
        for r in range(1, D):
            v = arr[r][c]
            if v == prev:
                stack += 1
            else:
                stack = 1
                prev = v
            if stack >= K:
                break
        else:

            return False

    return True


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())  # D: 두께(y축/행), W: 가로크기(x축/열), K: 합격기준
    arr = [list(map(int, input().split())) for _ in range(D)]  # 1과 0으로 이루어진 2차원 배열

    min_v = float('inf')
    DFS(0, D, W, K, arr, 0)

    print(f"#{tc} {min_v}")