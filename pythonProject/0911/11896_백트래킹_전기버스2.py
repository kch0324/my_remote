# 끝까지 못가면 리턴
# 최소횟수 넘어가면 리턴
# 종점 도착하면 최솟값 갱신후 리턴

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))   # 일단 배열로 받고 첫번째 요소를 N으로 분리
    N = arr[0]      # N: 정류장 수
    arr = arr[1:]   # arr:

    min_v = float('inf')

    def bus(depth, battery, charge):
        global min_v
        if battery < 0:  # 충전량 모자라지면 리턴
            return
        
        if depth == N - 1:  # 정류장은 인덱스 0부터 시작 N-1번이 마지막 정류장
            min_v = min(min_v, charge)
            return
        
        if charge >= min_v: # 최소횟수 넘어가면 리턴
            return

        # 현재위치에서 충전함과 충전안함 두가지로 나뉨
        bus(depth + 1, battery - 1, charge)  # 충전안함
        bus(depth + 1, arr[depth] - 1, charge + 1) # 충전함
    
    bus(1, arr[0] - 1, 0)   # 출발점에서는 무조건 충전한 상태로 시작
    print(f"#{tc} {min_v}")