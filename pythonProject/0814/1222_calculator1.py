for tc in range(1, 11):
    N = int(input())    # N: 문자열의 길이
    my_str = input()    # my_str: 문자열

    icp = {'+': 1}
    isp = {'+': 1}

    postfix = []
    stack = []
    for token in my_str:
        if token.isdecimal():   # 토큰이 숫자일 경우 후위표기에 추가
            postfix.append(int(token))
        else:   # 토큰이 연산자일 경우
            while stack:    # 스택안에 다른 연산자가 있다면 우선순위를 비교함
                k = stack.pop()
                if isp[k] < icp[token]: # 비교해서 바깥 토큰 우선순위가 크면 스택에 삽입
                    stack.append(k)
                    break
                else:   # 아니라면 스택안에 우선순위가 더 높을때까지 빼서 후위표기에 추가
                    postfix.append(k)
            stack.append(token)
    while stack:    # 문자열을 다 순회하고 스택에 남아있는게 있다면 후위표기에 추가
        postfix.append(stack.pop())

    stack = []
    for token in postfix:
        if type(token) == int:
            stack.append(token)
        else:
            if token == '+':
                result = stack.pop() + stack.pop() 
                stack.append(result)

    print(f"#{tc} {stack.pop()}")