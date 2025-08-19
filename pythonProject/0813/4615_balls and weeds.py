T = int(input())
for tc in range(1, T + 1):
    string = input()    # 문자열로 인풋을 받음
    stack = []
    cnt = 0
    # 문자열 for 문으로 돌리면서 ( 가 나오면 push, 스택안에 ( 가 있다면 pop 해서 다음번과 비교
    for i in string:
        if stack:
            k = stack.pop()
            if i == ')' or i == '|':     # 비교해서 ) or | 면 cnt + 1 / ( 면 다시 이전것까지 push
                cnt += 1
            elif i == '(':
                stack.extend([k, i])
        else:
            if i == '(':
                stack.append(i)
            elif i == ')':    # 만약 스택에 ( 가 없는데 string에서 ) 가 나오면 그냥 cnt + 1
                cnt += 1
    print(f"#{tc} {cnt}")