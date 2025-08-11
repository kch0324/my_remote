T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    pal = [None] * M        # M의 길이만큼 담을 빈 1차원 리스트 생성
    qal = [None] * M

    for i in range(N):
        for p in range(N - M+1):
            for j in range(p, p + M):
                pal[j - p] = arr[i][j]      # N을 행우선 순회, M길이 만큼까지 1차원 리스트 pal에 할당
                qal[j - p] = arr[j][i]      # N을 열우선 순회, M길이 만큼까지 1차원 리스트 qal에 할당

            for q in range(M):      # pal을 돌면서 대칭되는 index의 값이 같다면 마지막에 출력
                if pal[q] == pal[M-1 - q]:
                    pass
                else:
                    break
            else:
                print(f"#{tc} {''.join(pal)}")

            for q in range(M):      # qal을 돌면서 대칭되는 index의 값이 같다면 마지막에 출력
                if qal[q] == qal[M-1 -q]:
                    pass
                else:
                    break
            else:
                print(f"#{tc} {''.join(qal)}")