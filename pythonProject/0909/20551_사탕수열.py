T = int(input())
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())

    cnt = 0
    while B >= C:
        B -= 1
        cnt += 1
    while A >= B:
        A -= 1
        cnt += 1
    
    if B <= 0 or A <= 0:
        result = -1
    else:
        result = cnt
    
    print(f"#{tc} {result}")