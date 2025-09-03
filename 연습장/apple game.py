T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # NxN 격자
    arr = [list(map(int, input().split())) for _ in range(N)]   # NxN 2차원 리스트 (빈칸은 0, 자연수는 사과)

    apples = [0] * 11   # 사과 개수는 최대 10개 (카운팅 리스트)
    for y in range(N):
        for x in range(N):
            if arr[y][x] != 0:  # 사과면 해당 사과번호에 좌표를 튜플로 저장
                apples[arr[y][x]] = (y, x)
    apples = [x for x in apples if x != 0]  # 0을 제거해주고 첫번째 요소만 0을 추가해서 for 문의 범위로 사용할 수 있게 만듬
    apples = [0] + apples

    cnt = 0
    start = (0, 0)  # 시작지점 좌표 (y, x)
    pointer = 1     # 시작 포인터: 동-1 / 서-2 / 남-3 / 북-4
    for num in range(1, len(apples)):
        apple = apples[num]
        # 진행방향이 동쪽일때
        if pointer == 1:
            if start[0] > apple[0]:  # 사과가 출발지점보다 왼쪽에 있으면
                cnt += 3
                pointer = 4
            else:   # 출발지점보다 오른쪽에 있을때
                if start[1] < apple[1]:  # 출발지점보다 앞쪽에 있으면
                    cnt += 1
                    pointer = 3
                else:   # 출발지점보다 뒤쪽에 있으면
                    cnt += 2
                    pointer = 2

        # 진행방향이 서쪽일때
        elif pointer == 2:
            if start[0] < apple[0]:  # 왼쪽에 있으면
                cnt += 3
                pointer = 3
            else:   # 오른쪽에 있을때
                if start[1] > apple[1]:  # 앞쪽에 있으면
                    cnt += 1
                    pointer = 4
                else:   # 뒤쪽에 있으면
                    cnt += 2
                    pointer = 1

        # 진행방향이 남쪽일때
        elif pointer == 3:
            if start[1] < apple[1]:  # 왼쪽에 있으면
                cnt += 3
                pointer = 1
            else:   # 오른쪽에 있을때
                if start[0] < apple[0]:  # 앞쪽에 있으면
                    cnt += 1
                    pointer = 2
                else:   # 뒤쪽에 있으면
                    cnt += 2
                    pointer = 4

        # 진행방향이 북쪽일때
        elif pointer == 4:
            if start[1] > apple[1]:  # 왼쪽에 있으면
                cnt += 3
                pointer = 2
            else:   # 오른쪽에 있을때
                if start[0] > apple[0]:  # 앞쪽에 있으면
                    cnt += 1
                    pointer = 1
                else:   # 뒤쪽에 있으면
                    cnt += 2
                    pointer = 3

        start = apple   # 사과를 먹은 좌표로 출발지점 갱신

    print(f"#{tc} {cnt}")