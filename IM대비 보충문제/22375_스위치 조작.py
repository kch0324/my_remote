T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    cnt = 0

    for i in range(N):
        if Ai[i] != Bi[i]:   # 두 배열이 다르다면
            for j in range(i, N):   # i부터 끝까지 0은 1, 1은 0으로 바꾼다
                Ai[j] = 1 - Ai[j]
            cnt += 1

    print(f"#{tc} {cnt}")
#############################################################################################################
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    current = A[:] # 현재상태
    cnt = 0

    for i in range(N):
        if current[i] != B[i]: # 현재 상태와 B의 상태가 다르다면
            for j in range(i, N): # i부터 끝까지 바꾼다
                current[j] = 1 - current[j]
            cnt += 1

    print(f'#{tc} {cnt}')