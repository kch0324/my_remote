# 주사위 3개, 중복순열, 합이 10 이하인 케이스의 경우의 수

result = 0
def solution(depth, sums):
    global result
    if sums > 10:   # 가지치기
        return

    if depth == 3:
        # if sums <= 10:    # 이렇게 써도 되긴 하는데 어차피 위에서 아닌 경우가 쳐짐
        #     result += 1
        result += 1
        return

    for num in range(1, 7):
        solution(depth + 1, sums + num)

solution(0, 0)
print(result)