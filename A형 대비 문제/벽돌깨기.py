# 열우선순회 같은 거..
'''
함수 1번 호출 시 일어나는 일
dfs(j, arr, N, W, H, cnt) # j: 가로 열, N: 구슬 횟수, W: 폭, H: 높이, cnt: 현재 구슬 횟수(재귀 횟수)
1. 해당 열을 순회해서 처음으로 0이 아닌 것을 찾음.

2. 터뜨림(재귀함수) -> 4방향 델타를 p만큼 p는 해당 (i,j)요소의 값
3. 터뜨린 델타에 있는 숫자만큼 4방향 델타가 터짐(재귀) return 시점은 각 함수의 p만큼 도달했을때

4. 아무 순회로 배열 카운트해서 0이 아닌 수랑 min_v 비교해서 갱신

5. 블록이 모두 터진 이후 열우선 순회로 스택에 넣어준뒤 0을 제거하고 열의 아래부터 후입선출

6.
backup = [row[:] for row in arr]
for j in range(W):
    dfs(j, arr, N, W, H, cnt + 1)
    arr = backup
'''
def DFS(c, arr, N, W, H, cnt):
    global min_v
    if cnt == N:    # 벽돌깨기가 끝나면 최솟값 갱신
        temp = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0:
                   min_v = min(min_v, temp)

    elif cnt > 0: # 카운트가 0이상일때만 벽돌깨기를 시행
        for i in range(H):
            if arr[i][c] != 0:  # 위에서부터 첫번째 벽돌을 터뜨림
                bomb(i, c, W, H)
                break
        else:   # 해당 열에 벽돌이 없으면 나감
            return

        for j in range(W):  # 열을 위에서부터 스택에 담고 0을 지운후 그 스택을 열 아래서부터 덮어씌움
            stack = []
            for i in range(H):
                stack.append(arr[i][j])
            stack = [x for x in stack if x != 0]
            for i in reversed(range(H)):
                if not stack:
                    break
                arr[i][j] = stack.pop()

    backup = [row[:] for row in arr]    # 다음 depth로 가기전 arr의 백업본을 복사해두고 돌아오면 원복
    for c in range(W):
        DFS(c, arr, N, W, H, cnt + 1)
        arr = backup


def bomb(i, j, W, H):
    Di = [0, 0, -1, 1]
    Dj = [1, -1, 0, 0]
    val = arr[i][j]      # 현재 블록 값
    arr[i][j] = 0        # 자기 자신 제거

    if val <= 1:         # 값이 1이면 확산 없음
        return

    # 4방향으로 확산
    for k in range(4):
        Ni, Nj = i, j
        for step in range(1, val):   # val-1칸 만큼 확산
            Ni += Di[k]; Nj += Dj[k]
            if 0 <= Ni < H and 0 <= Nj < W:
                if arr[Ni][Nj] > 1:        # 또 터질 수 있는 블록이면 재귀
                    bomb(Ni, Nj, W, H)
                arr[Ni][Nj] = 0            # 블록 제거
            else:
                break


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split()) # N: 구슬 횟수, W: 폭, H: 높이
    arr = [list(map(int, input().split())) for _ in range(H)]   # arr: 벽돌 배열

    min_v = float('inf')
    DFS(0, arr, N, W, H, 0)

    print(f"{tc} {min_v}")