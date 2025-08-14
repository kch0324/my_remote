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