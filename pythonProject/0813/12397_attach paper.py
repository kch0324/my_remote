# f(0) = 1
# f(1) = 1
# f(2) = 3
# f(3) = 5
# f(4) = 11
#
# f(2) = f(1) + f(0) * 2
# f(3) = f(2) + f(1) * 2
# f(4) = f(3) + f(2) * 2
# f(n) = f(n-1) + f(n-2) * 2
def get_paper(n):
    while n <= N:
        if n == 0 or n == 1:
            return 1
        else:
            return get_paper(n-1) + get_paper(n-2) * 2

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f"#{tc} {get_paper(N/10)}")