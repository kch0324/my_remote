T = int(input())
for tc in range(1, T+1):
    N = int(input())
 
    lst = [[] for _ in range(N)]
 
    for i in range(0, N):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            lst[i].append(j)
 
    P = int(input())
    result = []
 
    for _ in range(1, P+1):
        plus = 0
        c = int(input())
        for i in range(0, N):
            if c in lst[i]:
                plus += 1
        result.append(plus)
    print(f"#{tc} {' '.join(map(str, result))}")
##########################################################################################################
# DAT 자료구조로 풀기
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 버스 노선의 수

    # DAT 배열생성(인덱스를 1에서 5000)
    dat = [0] * 5001

    for _ in range(N):
        a, b = map(int, input().split())
        # A정류장 부터 B정류장까지 counting
        for i in range(a, b + 1):
            dat[i] += 1
    
    P = int(input())
    result = [] # 빈배열

    for _ in range(P):
        C = int(input())
        result.append(dat[C])

    print(f'#{tc}', end = ' ')
    print(*result)
    

