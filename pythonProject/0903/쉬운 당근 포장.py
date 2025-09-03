'''
[1, 1, 1, 2, 3, 3, 4, 5, 5]
순서를 가진 개수만큼의 용량
1은 3개, 2는 1개, 3은 2개, 4는 2개, 5는 2개

카운팅 리스트
c_arr = [0, 3, 1, 2, 2, 2] -> 0 제거 [3, 1, 2, 2, 2]
순서대로 상자에 담아야 하며, 각 상자에 들어가면 더해줌, 각 상자의 차가 최소여야함
[3] [1 2 2] [2]     차이: 3
[3] [1 2] [2 2]     차이: 1
[3 1] [2] [2 2]     차이: 2

[1 3 2 2]
[1] [3 2] [2]   차이: 4
[1 3] [2] [2]   차이: 2

투포인터
left_v = 0
mid_v = sum(전체) - left_v - right_v
right_v = 0
'''
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Ci = list(map(int, input().split()))

    num = max(Ci)
    count_list = [0] * (num + 1)   # 당근 크기별 개수 카운팅리스트
    for i in Ci:
        count_list[i] += 1
    count_list = [x for x in count_list if x != 0]  # 모든 0을 제거

    M = len(count_list)
    if M < 3:   # 당근 종류가 3개 미만이면 불가능
        result = -1
    elif M == 3:
        result = max(count_list) - min(count_list)
    else:
        min_v = float('inf')
        total = sum(count_list)
        left_v = count_list[0]  # 왼쪽박스는 첫번째값이 무조건 포함
        right_v = count_list[M - 1] # 오른쪽 박스는 마지막값이 무조건 포함

        l = 0; r = M - 1
        while l < r - 1:    # 3개의 박스에 모두 담아져 있는 경우 동안만
            mid_v = total - left_v - right_v
            temp = max(left_v, right_v, mid_v) - min(left_v, right_v, mid_v)    # 박스들간의 당근 개수 차
            min_v = min(min_v, temp)    # 당근 개수 차 최솟값 갱신
            if min(left_v, right_v, mid_v) == mid_v:    # 가운데 박스가 제일 작아지면 종료
                break
            elif left_v == right_v: # 왼쪽과 오른쪽 박스가 같으면 가운데 박스 요소를 비교해서 어디에 추가할지 결정
                if count_list[l+1] <= count_list[r-1]:
                    l += 1
                    left_v += count_list[l]
                else:
                    r -= 1
                    right_v += count_list[r]
            elif min(left_v, right_v, mid_v) == left_v:   # 왼쪽 박스가 제일 작으면 한 종류 추가해줌
                l += 1
                left_v += count_list[l]
            elif min(left_v, right_v, mid_v) == right_v:  # 오른쪽 박스가 제일 작으면 한 종류 추가해줌
                r -= 1
                right_v += count_list[r]
        result = min_v

    print(f"#{tc} {result}")