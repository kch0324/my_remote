# 교차하려면 a전선의 왼쪽은 b전선의 왼쪽보다 낮고, a전선의 오른쪽은 b전선의 오른쪽보다 높아야 함
# 높이가 같은 경우는 없음
# -> 왼쪽의 차와 오른쪽의 차가 서로 부호(양,음수)가 달라야 교차함

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        Ai, Bi = map(int, input().split())
        arr += [(Ai, Bi)]
    
    # 조합
    cnt = 0
    def recur(start, path):
        global cnt
        # 2개를 뽑으면 종료 / 왼쪽의 차와 오른쪽의 차가 서로 부호가 다르면 교차 -> 서로 곱해서 음수
        if len(path) == 2:
            if (path[0][0] - path[1][0]) * (path[0][1] - path[1][1]) < 0:
                cnt += 1
            return
        for i in range(start, N):
            path.append(arr[i])
            recur(i + 1, path)
            path.pop()  # 원복

    recur(0, [])

    print(f"#{tc} {cnt}")