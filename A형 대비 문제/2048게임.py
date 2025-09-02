# 가로 방향(좌, 우) : 행우선 순회 / 세로 방향(상, 하) : 열우선 순회
# 순회하며 행 or 열마다 스택에 넣어서 이전 요소와 다음 요소가 같으면 합쳐서 덱에 넣음
# 각 행 or 열 순회가 끝나면 덱에 있는 요소들을 선입선출로 출력할 공배열에 저장

from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N, S = input().split()  # N: 격자크기, S: 방향
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]   # NxN 배열
    result = [[0] * N for _ in range(N)]    # 출력할 정답

    if S == 'left':     # 왼쪽부터 비교
        for i in range(N):
            stack = []
            deq = deque()
            for j in range(N):
                token = arr[i][j]
                if token == 0:
                    continue
                if not stack:
                    stack.append(token)
                elif stack[-1] == token:    # 비교해서 다음 요소와 같으면 합쳐서 덱에 넣음
                    deq.append(stack.pop() + token)
                else:   # 같지 않으면 앞 요소만 덱에 넣고 뒷 요소는 스택에 넣어서 다음번에 비교
                    deq.append(stack.pop())
                    stack.append(token)
            while stack:    # 루프 끝난 뒤 마지막 요소 스택에 남아있으면 덱으로 넣음
                deq.append(stack.pop())
            for j in range(N):  # 출력할 공집합에 해당 덱을 선입선출로 덮어씌움
                if not deq:
                    break
                result[i][j] = deq.popleft()

    elif S == 'right':  # 오른쪽부터 비교
        for i in range(N):
            stack = []
            deq = deque()
            for j in reversed(range(N)):
                token = arr[i][j]
                if token == 0:
                    continue
                if not stack:
                    stack.append(token)
                elif stack[-1] == token:  # 비교해서 다음 요소와 같으면 합쳐서 덱에 넣음
                    deq.append(stack.pop() + token)
                else:  # 같지 않으면 앞 요소만 덱에 넣고 뒷 요소는 스택에 넣어서 다음번에 비교
                    deq.append(stack.pop())
                    stack.append(token)
            while stack:  # 루프 끝난 뒤 마지막 요소 스택에 남아있으면 덱으로 넣음
                deq.append(stack.pop())
            for j in reversed(range(N)):  # 출력할 공집합에 해당 덱을 선입선출로 덮어씌움
                if not deq:
                    break
                result[i][j] = deq.popleft()

    elif S == 'up':     # 위쪽부터 비교
        for j in range(N):
            stack = []
            deq = deque()
            for i in range(N):
                token = arr[i][j]
                if token == 0:
                    continue
                if not stack:
                    stack.append(token)
                elif stack[-1] == token:  # 비교해서 다음 요소와 같으면 합쳐서 덱에 넣음
                    deq.append(stack.pop() + token)
                else:  # 같지 않으면 앞 요소만 덱에 넣고 뒷 요소는 스택에 넣어서 다음번에 비교
                    deq.append(stack.pop())
                    stack.append(token)
            while stack:  # 루프 끝난 뒤 마지막 요소 스택에 남아있으면 덱으로 넣음
                deq.append(stack.pop())
            for i in range(N):  # 출력할 공집합에 해당 덱을 선입선출로 덮어씌움
                if not deq:
                    break
                result[i][j] = deq.popleft()

    elif S == 'down':   # 아래쪽부터 비교
        for j in range(N):
            stack = []
            deq = deque()
            for i in reversed(range(N)):
                token = arr[i][j]
                if token == 0:
                    continue
                if not stack:
                    stack.append(token)
                elif stack[-1] == token:  # 비교해서 다음 요소와 같으면 합쳐서 덱에 넣음
                    deq.append(stack.pop() + token)
                else:  # 같지 않으면 앞 요소만 덱에 넣고 뒷 요소는 스택에 넣어서 다음번에 비교
                    deq.append(stack.pop())
                    stack.append(token)
            while stack:  # 루프 끝난 뒤 마지막 요소 스택에 남아있으면 덱으로 넣음
                deq.append(stack.pop())
            for i in reversed(range(N)):  # 출력할 공집합에 해당 덱을 선입선출로 덮어씌움
                if not deq:
                    break
                result[i][j] = deq.popleft()


    print(f"#{tc}")
    for _ in result:
        print(*_)