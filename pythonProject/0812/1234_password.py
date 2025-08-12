for tc in range(1, 11):
    N, string = map(str, input().split())
    stack = []
    for i in string:
        if not stack:
            stack.append(i)
        else:
            k = stack.pop()     # 스택의 마지막 요소 pop하고 k에 저장
            if i == k:     # 같은 문자열이 오면 스택의 해당 문자열 pop된 상태 유지
                pass
            else:       # 다른 문자열이 오면 pop했던 문자와 다음 문자를 차례로 스택에 push
                stack.append(k)
                stack.append(i)
    print(f"#{tc} ", *stack, sep="")