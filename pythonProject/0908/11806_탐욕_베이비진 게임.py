from collections import Counter

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    p1_set, p2_set = [], []
    for i in range(12):
        if i % 2 == 0:
            p1_set.append(arr[i])
        else:
            p2_set.append(arr[i])

    p1, p2 = [], []
    winner = []
    def get_winner(num, p, p_set):
        for j in range(6):  # 플레이어 1
            p.append(p_set[j])

            if Counter(p).most_common()[0][1] >= 3:  # 가장 많은 중복된 수가 3개 이상이면 triplet
                winner.append((num, j))   # winner에 플레이어 번호와 현재 라운드 튜플로 추가
                return
            
            else:
                sort_p = sorted(set(p))
                for i in range(len(sort_p) - 2):    # 중복된 수 제외하고 정렬했을때 3번 이상 1차이나는 수가 나오면 run
                    if sort_p[i] + 1 == sort_p[i + 1] and sort_p[i + 1] + 1 == sort_p[i + 2]:
                        winner.append((num, j))
                        return
    
    get_winner(1, p1, p1_set)
    get_winner(2, p2, p2_set)

    if len(winner) == 0:
        result = 0
    elif len(winner) == 2:
        winner.sort(key=lambda x: x[1])
        result = winner[0][0]
    else:
        result = winner.pop()[0]
    
    print(f"#{tc} {result}")