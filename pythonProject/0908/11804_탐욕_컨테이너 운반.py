T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N: 화물 수, M: 트럭 수
    dump = list(map(int, input().split()))   # 화물 무게 배열
    truck = list(map(int, input().split())) # 트럭 적재용량 배열

    dump.sort()
    truck.sort()

    result = 0
    while dump:
        weight = dump.pop()
        while truck:
            volume = truck.pop()
            if weight <= volume:
                result += weight
                break
            else:
                truck.append(volume)
                break
    
    print(f"#{tc} {result}")
