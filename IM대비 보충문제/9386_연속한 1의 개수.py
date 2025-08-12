T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    max_c = 0
    temp_c = 0
    for i in range(N):
        if arr[i] == 1:
            temp_c += 1
            if max_c < temp_c:
                max_c = temp_c
        else:
            temp_c = 0
    print(f"#{tc} {max_c}")
###################################################################################################
            
# 그리디(욕심쟁이) 알고리즘
# 완전탐색으로 풀면 모든 경우의수를 탐색해야되니까 시간이 오래걸린다.(시간초과)
# 최적의 선택을 한다.
# 나만의 전략대로 문제를 푼다.

# 전략 : '1'이 등장하면 counting하면서 최대값 갱신

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    sequence = input()

    max_cnt = 0
    cnt = 0
    # for문 순회 1. 인덱싱 방식
    # 2. iterator 방식 순회
    for seq in sequence: # 파이써닉한 방식()
        if seq == '1':
            cnt += 1 # counting
            max_cnt = max(max_cnt, cnt) # 최대값 갱신
        else:
            cnt = 0 # count 초기화

    print(f'#{tc} {max_cnt}')