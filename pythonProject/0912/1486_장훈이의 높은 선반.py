import sys
sys.stdin = open("input.txt")

# 종료조건:  N명의 모든 점원을 고려했을 때
# - 가지치기: N이 B보다 높아진 경우
# 가지의 수:
# - 점원을 탑에 포함 시키는 경우 or 안시키는 경우
def recur(cnt, total_height):
    global min_v

    if total_height >= B:
        min_v = min(min_v, total_height)
        return
    if cnt == N:
        return
    
    recur(cnt + 1, total_height + heights[cnt])  # 탑에 포함 시키는 경우
    recur(cnt + 1, total_height)  # 탑에 포함 안시키는 경우


T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    min_v = float('inf')
    
    recur(0, 0)
    print(f"{tc} {min_v}")
