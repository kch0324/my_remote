T = int(input())
for tc in range(1, T + 1):
    A, B = map(str, input().split())
    n, m = len(A), len(B)

    def brute_typing(A, B):
        cnt = 0     # 텍스트에 패턴이 들어있는 횟수
        for i in range(n - m + 1):     # brute force로 탐색
            for j in range(m):
                if A[i + j] != B[j]:
                    break
            else:
                cnt += 1
        return n - (m - 1) * cnt      # 텍스트 길이에 패턴의 길이 - 1 을 중복된 만큼 뺌

    print(f"#{tc} {brute_typing(A, B)}")