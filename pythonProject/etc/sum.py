for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]     # 100 X 100의 배열 생성
    max_r = 0       # 행과열, 대각선들의 합중 최댓값의 초기값
    max_c = 0
    d1 = 0
    d2 = 0

    for r in range(100):    # 현재행의 합, 현재열의 합 초기값
        temp_r = 0
        temp_c = 0
        d1 += arr[r][r]      # 현재대각선1, 현재대각선2의 합들을 +
        d2 += arr[r][99 - r]

        for c in range(100):    # 각 합에 현재행, 현재열의 합들을 +
            temp_r += arr[r][c]
            temp_c += arr[c][r]

        if max_r < temp_r:      # 최댓값 갱신
            max_r = temp_r
        if max_c < temp_c:
            max_c = temp_c

     max_lst = [max_r, max_c, d1, d2]     # 4개의 종류의 최댓값중 가장 최댓값
    max_v = max_lst[0]
    for mx in max_lst:
        if max_v < mx:
            max_v = mx

    print(f"#{t} {max_v}")
