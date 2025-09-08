from collections import Counter
T = int(input())
for tc in range(1, T + 1):
    arr, M = input().split()
    arr, M = list(arr), int(M)
    N = len(arr)
    max_v = 0
    visited = set()  # (depth, tuple(arr)) 저장
    def recur(depth, arr):
        global max_v
 
        state = (depth, tuple(arr))     # 교환횟수와 현재배열을 visited에 튜플로 저장
        if state in visited:    # 같은 교환횟수만큼 교환했는데 숫자가 같다면 가지치기
            return
        visited.add(state)
 
        if depth == M:  # 끝까지 가면 최댓값 갱신후 리턴
            num = int("".join(arr))
            max_v = max(max_v, num)
            return
 
        # 최대 교환횟수 전에 이미 최댓값이 된 경우, 남은 교환횟수를 계산하여 가지치기
        for i in range(N-1):
            if arr[i] < arr[i + 1]:
                break
        else:
            if (M - depth) % 2 == 0:    # 짝수면 현재수 그대로 리턴
                num = int("".join(arr))
                max_v = max(max_v, num)
                return
            else:   # 홀수일때
                if Counter(arr).most_common(1)[0][1] != 1:  # 현재수에 중복된 숫자가 있으면 현재수 그대로 리턴
                    num = int("".join(arr))
                    max_v = max(max_v, num)
                    return
                else:
                    arr[N-2], arr[N-1] = arr[N-1], arr[N-2]   # 없으면 현재수에 마지막 두자리를 바꿔준 후 리턴
                    num = int("".join(arr))
                    max_v = max(max_v, num)
                    arr[N-2], arr[N-1] = arr[N-1], arr[N-2]   # 원복
                    return
 
 
        for i in range(N):
            for j in range(i + 1, N):
                arr[i], arr[j] = arr[j], arr[i]
                recur(depth + 1, arr)
                arr[i], arr[j] = arr[j], arr[i]
        
 
    recur(0, arr)
    print(f"#{tc} {max_v}")