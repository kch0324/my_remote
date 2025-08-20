T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 화덕사이즈, M: 피자개수
    pizza = list(map(int, input().split()))   # C 피자(치즈)들의 배열
    N += 1  # 큐사이즈 = 화덕사이즈 + 1

    def enqueue(item):
        global tail
        if (tail + 1) % N == head:
            return
        tail = (tail + 1) % N
        Q[tail] = item

    def dequeue():
        global head
        if head == tail:
            return
        head = (head + 1) % N
        return Q[head]

    Q = [None] * N
    out = []    # 화덕에서 나온 피자들의 배열
    head = tail = 0

    i = 1   # i: pizza의 인덱스
    enqueue(i)
    while head != tail:
        while (tail + 1) % N != head:   # 큐에 자리가 없지 않으면 pizza에서 i를 순서대로 꺼내 큐에 넣음
            if i >= M:
                break
            i += 1
            enqueue(i)

        num = dequeue()
        if pizza[num - 1] // 2 == 0:  # C가 0이면 큐에서 빼고 넘어감
            out.append(num)
        else:   # C가 남아있다면 2로 나눠주고 다시 큐에 넣음
            pizza[num - 1] = pizza[num - 1] // 2
            enqueue(num)

    print(f"#{tc} {out.pop()}")