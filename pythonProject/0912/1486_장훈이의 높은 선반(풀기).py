# 목표 높이: B
# N개의 수들 중 임의의 개수만큼 더해서 B이상이 된 것 중 가장 낮은 것
# 가장 낮은 것과 B의 차를 답으로 출력

# 기저조건: 마지막 점원까지 고려했으면 합해진 수들을 min_v와 비교갱신 후 컷
# 재귀방법: 해당 점원을 포함하는지, 포함하지 않는지
# 가지치기: 현재 합해진 수들이 >= B이면 컷

def recur(depth, total_height):
    global min_v
    if depth > N:
        if total_height >= B:
            min_v = min(min_v, total_height)
        return
    
    if total_height >= min_v:
        return
    recur(depth + 1, total_height)  # 현재점원 포함 x
    recur(depth + 1, total_height + arr[depth])  # 현재점원 포함 o

        
T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())    # N: 점원들 수, B: 목표 높이
    arr = [0] + list(map(int, input().split()))   # arr: 점원들 키를 가진 배열(1번부터 사용)
    min_v = float('inf')

    recur(1, 0)
    print(f"#{tc} {min_v - B}")