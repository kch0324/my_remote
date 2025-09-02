# i: 행(재귀횟수), D: D까지 재귀(두께), W: 가로크기, K: 합격기준, arr: 배열, cnt: 약품 투입횟수
def DFS(i, D, W, K, arr, cnt):
    global min_v
    if check(arr, D, W, K):  # 합격기준 달성했는지 확인후 최소 시행횟수 갱신
        min_v = min(min_v, cnt)
    if i >= D:   # 끝까지 가면 탈출
        return
    if cnt >= min_v:  # 최소값보다 시행횟수 많아지면 탈출
        return
    copy_arr = arr[i]  # 1. 약품 투입 안하고 다음 층 넘어가는 경우
    DFS(i + 1, D, W, K, arr, cnt)

    for p in range(2):  # 2. 약품 투입 하는 경우 (0일때 / 1일때)
        arr[i] = [p] * W
        DFS(i + 1, D, W, K, arr, cnt + 1)
        arr[i] = copy_arr

def check(arr, D, W, K):
    for j in range(W):  # 열우선순회로 각열이 K만큼 연속된 수가 있는 지 확인
        stack = [arr[0][j]]  # 첫번째 열 요소 넣어줌
        for i in range(1, D):
            token = arr[i][j]
            if stack[-1] == token:  # 다음 요소가 스택의 요소와 같으면 push
                stack.append(token)
            else:
                stack.clear()   # 다르면, 스택을 비우고 요소를 push
                stack.append(token)
            if len(stack) >= K: # K개 이상 연속된 요소가 있으면 다음 열로 넘어감
                break
        else:   # K개 이상 연속된 요소가 없이 열순회가 종료되면 False
            return False
    return True # 모든 열에 K개 이상 연속된 요소가 있으면 True


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split()) # D: 두께(y축/행), W: 가로크기(x축/열), K: 합격기준
    arr = [list(map(int, input().split())) for _ in range(D)]   # 1과 0으로 이루어진 2차원 배열

    min_v = float('inf')
    DFS(0, D, W, K, arr, 0)
    
    print(f"#{tc} {min_v}")