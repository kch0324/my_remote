# 중복 순열
# [0, 1, 2] 3개의 카드가 존재 -> 2개를 뽑는다.

path = []   # used, visited... --> 뽑은 카드들을 저장
used = [False] * 4
# 기저조건(종료조건) : 2개의 카드를 모두 뽑았다면 종료
# - 시작점 : 0개의 카드를 고른 상태부터 시작
# 다음 재귀호출 구조 : [0, 1, 2] 카드 중 하나를 고른다.
def recur(cnt):
    if cnt == 2:
        print(path)
        return
    for i in range(3):
        if used[i]:
            continue
        used[i] = 1
        path.append(i)
        recur(cnt + 1)
        path.pop()
        used[i] = 0
recur(0)