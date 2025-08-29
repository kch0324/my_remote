# LVR 중위순회로 풀수 있을까
# V가 완성되면 넘긴다 -> 후위순회: 그러면 후위순회로 연산자랑 숫자를 받아서 left() 연산자 right() 하면?

def operate(op, tup):   # 연산자 계산 함수
    if op == '+':
        return tup[0] + tup[1]
    if op == '-':
        return tup[0] - tup[1]
    if op == '*':
        return tup[0] * tup[1]
    if op == '/':
        return tup[0] // tup[1]

def get_calc(node):  # LRV 후위순회로 리프노드부터 값을 node까지 더해서 가져옴
    if node == 0:
        return 0
    l = get_calc(left[node])
    r = get_calc(right[node])
    if type(val[node]) == int:  # 값이 정수형이면 그냥 반환
        return val[node]
    else:   # 값이 연산자면 연산해서 반환
        tup = (l, r)
        return operate(val[node], tup)

for tc in range(1, 11):
    N = int(input())
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    val = [0] * (N + 1)

    for i in range(N):
        arr = list(input().split())
        if len(arr) > 2:    # 연산자 정점이면 간선할당, 값 할당
            node, op, l, r = int(arr[0]), arr[1], int(arr[2]), int(arr[3])
            left[node], right[node], val[node] = l, r, op
        else:   # 정수 정점이면 값만 할당
            node, num = int(arr[0]), int(arr[1])
            val[node] = num

    result = get_calc(1)
    print(f"#{tc} {result}")