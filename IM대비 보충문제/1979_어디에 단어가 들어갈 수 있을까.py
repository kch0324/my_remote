T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
     
    cnt = 0
    stack_r = []
    stack_c = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:   # 행우선 순회
                stack_r.append(arr[i][j])
                 
            else:   # arr[i][j] == 0일 경우
                if len(stack_r) == K:
                    cnt += 1
                stack_r.clear()
             
             
            if arr[j][i] == 1:   # 열우선 순회
                stack_c.append(arr[j][i])
                 
            else:
                if len(stack_c) == K:
                    cnt += 1
                stack_c.clear()
        # 행렬의 끝까지 도달했을 경우
        if len(stack_r) == K:
            cnt += 1
        if len(stack_c) == K:
            cnt += 1
        stack_r = [] ; stack_c = []
     
    print(f"#{tc} {cnt}")
######################################################################################################
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        cnt = 0
        # 행 검사
        for j in range(N):
            if puzzle[i][j] == 1: cnt += 1
            if puzzle[i][j] == 0 or j == N - 1: # 0이 나왔거나 좌표끝
                if cnt == K: # 지금까지 센 cnt와 K를 비교
                    result += 1
                cnt = 0 # cnt 초기화

        # 열 검사
        for j in range(N):
            if puzzle[j][i] == 1: cnt += 1
            if puzzle[j][i] == 0 or j == N - 1:
                if cnt == K:
                    result += 1
                cnt = 0

    print(f'#{tc} {result}')