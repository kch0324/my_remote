T = int(input())
for tc in range(1, T + 1):
    postfix = list(input().split())
    
    def postcalc(postfix):
        stack = []
        for token in postfix:
            if token.isdecimal():
                stack.append(int(token))
            elif token == '.':
                break
            else:
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    if token == '+':
                        result = a + b
                    elif token == '-':
                        result = a - b
                    elif token == '*':
                        result = a * b
                    elif token == '/':
                        result = a // b
                    stack.append(result)
                else:
                    return 'error'
        return stack.pop()
    
    print(f"#{tc} {postcalc(postfix)}")