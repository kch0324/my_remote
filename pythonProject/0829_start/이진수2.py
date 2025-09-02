# 1/2 = 0.5  1/4 = 0.25  1/8 = 0.125
T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    i = 1
    result = ''
    while N:
        result += str(int(N // (1/2**i)))
        N %= (1/2**i)
        i += 1
    if len(result) >= 13:
        result = 'overflow'

    print(f"#{tc} {result}")