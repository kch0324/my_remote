T = int(input())
for tc in range(1, T+1):
    string = input()
    stack = []
    for i in string:
        if not stack:    # 첫 문자의 경우 그냥 스택에 push (인덱스 에러 방지)
            stack.append(i)
        else:
            k = stack.pop()     # 미리 전 문자 pop해서 k에 할당
            if k == i:    # k와 현재 문자가 같다면 두가지 문자 모두 삭제
                pass
            else:       # k와 현재 문자가 다르다면 다시 k부터 현재문자 차례로 push
                stack.append(k)
                stack.append(i)
    print(f"#{tc} {len(stack)}")