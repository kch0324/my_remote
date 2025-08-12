T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    stack = [0] * N
    top = -1

    for i in arr:
        if i != 0:
            top += 1
            stack[top] = i
        else:
            top -= 1
            stack[top+1] = 0
    print(f"#{tc} {sum(stack)}")