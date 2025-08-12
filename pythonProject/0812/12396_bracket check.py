T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input()))
    stack = []
    dic = {'(': ')', '{': '}'}
    ans = 1
    for i in arr:
        if i in dic.keys():     # arr에 열린 괄호가 있는 경우 stack에 push
            stack.append(i)
        elif i in dic.values():     # arr에 닫힌 괄호가 있는 경우
            if not stack:     # stack에 열린 괄호가 없다면 에러
                ans = 0
                break
            k = stack.pop()
            if dic[k] != i:     # stack의 열린괄호 종류와 arr의 닫힌 괄호 종류가 다를 경우 에러
                ans = 0
                break
    if len(stack) != 0:     # 열린 괄호가 남아있는 경우 에러
        ans = 0
    print(f"#{tc} {ans}")