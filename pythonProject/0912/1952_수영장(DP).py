T = int(input())
for tc in range(1, T + 1):
    # 일,월,3달,연간 이용권의 가격을 각각 정수로 받음
    day_cost, month_cost, month3_cost, year_cost = map(int, input().split())
    # days: 해당 월에 수영장을 이용한 일 수 (1번 인덱스부터 사용)
    days = [0] + list(map(int, input().split()))
    
    min_cost = [0] * 13   # min_cost: 해당 월까지 최소 누적비용 dp (1번 인덱스부터 사용)
    min_cost[1] = min(day_cost * days[1], month_cost)
    min_cost[2] = min_cost[1] + min(day_cost * days[1], month_cost)

    for i in range(3, 13):
        min_cost[i] = min(min_cost[i-1] + min(day_cost * days[i], month_cost),
                          min_cost[i-3] + month3_cost)
    
    result = min(min_cost[12], year_cost)
    print(f"#{tc} {result}")