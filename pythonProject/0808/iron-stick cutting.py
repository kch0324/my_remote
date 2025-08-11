# ( = 1,    ) = -1
# 직전 수 1, 다음 수 -1  =  레이저
# 쇠막대기는 사이에 있는 레이저 개수 +1
# 레이저가 나오면 왼쪽에 몇개의 닫히지 않은 ( 가 있는지 파악

# 2. 이후 레이저 등장하면 왼쪽 ( * 1
# 3. 2번째 레이저 이후부터 정산전 새로운 ( 가 나타나면 + 1
T = int(input())
for tc in range(1, T+1):
    sstr = str(input())
    lst = []
    cnt = 0
    i = 0
    for a in sstr:
        if a == '(':
            lst.append(1)
        else:
            lst.append(-1)
    print(lst)

    while i < len(lst):
        if lst[i] == 1 and lst[i+1] == -1:
            lst.pop(i)
            lst[i] = 3
        else:
            i += 1
    print(lst)






