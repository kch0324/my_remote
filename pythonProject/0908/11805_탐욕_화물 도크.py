T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # N: 작업 개수
    arr = []
    for i in range(N):
        s, e = map(int, input().split())    # s: 시작시간, e: 종료시간
        arr += [(s, e)]    # arr: 각 작업의 (시작, 종료시간) 튜플을 요소로 하는 리스트
    
    arr.sort(key=lambda x: (x[1], x[0]))  # arr을 종료시간, 시작시간 순으로 정렬

    cnt = 0
    end_time = 0
    for i in range(N):
        if arr[i][0] >= end_time:   # 다음 작업의 시작시간이 이전 작업 종료시간 이상이라면
            cnt += 1
            end_time = arr[i][1]
    
    print(f"#{tc} {cnt}")