# 두개의 숫자열
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    if N < M:
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
    else:
        B = list(map(int, input().split()))
        A = list(map(int, input().split()))

    max_v = float('-inf')
    s = 0
    while s <= len(B)-len(A):
        temp = 0
        for i in range(len(A)):
            temp += A[i] * B[i + s]
        max_v = max(max_v, temp)
        s += 1

    print(f"#{tc} {max_v}")