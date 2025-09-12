T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_v = float('inf')
    path = []
    def recur(depth, total):
        global min_v
        if depth == N:
            min_v = min(min_v, total)
            return
        
        # 현재합이 최소합보다 커지면 가지치기
        if total >= min_v:
            return
        
        for i in range(N):
            if i in path:
                continue
            path.append(i)
            total += arr[depth][i]
            recur(depth + 1, total)
            total -= arr[depth][i]
            path.pop()
    
    recur(0, 0)
    print(f"#{tc} {min_v}")