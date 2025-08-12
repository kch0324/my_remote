TC = int(input())
def fact(n):
    if n <= 1:
        return 1
    else:
        n * fact(n-1)
print(fact(5))
# for tc in range(1, TC + 1):
#     N, M = map(int, input().split())
#     for n in range(N):
#         string = input()
