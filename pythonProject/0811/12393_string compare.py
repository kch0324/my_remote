T = int(input())
for tc in range(1, T + 1):
    N = input()
    M = input()
    def brute_force(N, M):
        for i in range(len(M) - len(N) + 1):
            for j in range(len(N)):
                if N[j] != M[i + j]:
                    break
            else:
                return 1
        return 0
    print(f"#{tc} {brute_force(N, M)}")
