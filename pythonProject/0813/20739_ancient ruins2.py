T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    max_v = 0
    for i in range(N):   # 행우선 순회
        for j in range(M):
            if arr[i][j] == 1:   # 1이 나오면 스택에 저장
                stack.append(1)
            else:
                if stack:    # 스택안에 1이 있던 경우
                    max_v = max(max_v, len(stack))   # max_v 갱신 후 stack 초기화
                    stack = []
        else:    # 마지막 열까지 도달했는데 1로 끝날 경우 max_v 갱신
            max_v = max(max_v, len(stack))
            stack = []

    for j in range(M):   # 열우선 순회
        for i in range(N):
            if arr[i][j] == 1:   # 1이 나오면 스택에 저장
                stack.append(1)
            else:
                if stack:    # 스택안에 1이 있던 경우
                    max_v = max(max_v, len(stack))   # max_v 갱신 후 stack 초기화
                    stack = []
        else:    # 마지막 열까지 도달했는데 1로 끝날 경우 max_v 갱신
            max_v = max(max_v, len(stack))
            stack = []

    if max_v < 2:    # 길이가 2 미만인 경우 0을 출력
        max_v = 0
    print(f"#{tc} {max_v}")