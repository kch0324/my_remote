# # A, J, Q, K 네종류의 카드 / 5장의 카드를 뽑아 나열 / 같은 종류의 카드가 세 장 연속으로 나오는 경우의 수는?
# # 중복순열
#
path = []
result = 0
def count_three():
    stack = [path[0]]
    for next_card in range(1, len(path)):
        if len(stack) >= 3:
            return True
        elif stack[-1] == path[next_card]:
            stack.append(path[next_card])
        else:
            stack.pop()
            stack.append(path[next_card])
    return False

def solution(depth):
    global result
    if depth == 5:
        # Todo: 연속된 3개가 나오면 counting
        if count_three():
            print(*path)
            result += 1
        return
    for card in ['A', 'J', 'Q', 'K']:
        path.append(card)
        solution(depth + 1)
        path.pop()

solution(0)
print(result)
