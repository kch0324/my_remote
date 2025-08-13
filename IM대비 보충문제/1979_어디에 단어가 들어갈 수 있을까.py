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
                stack_r.clear
            
            
            if arr[j][i] == 1:   # 열우선 순회
                stack_c.append(arr[j][i])
                
            else:
                if len(stack_c) == K:
                    cnt += 1
                stack_c.clear

        if len(stack_r) == K:
            cnt += 1
        if len(stack_c) == K:
            cnt += 1
        stack_r = stack_c = []
    
    print(f"#{tc} {cnt}")