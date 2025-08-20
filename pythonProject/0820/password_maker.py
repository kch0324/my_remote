def enqueue(item):
    global tail
    if (tail + 1) % 9 == head:
        return
    tail = (tail + 1) % 9
    Q[tail] = item


def dequeue():
    global head
    if head == tail:
        return
    head = (head + 1) % 9
    return Q[head]

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    Q = [1] + arr   # 원형 큐 생성

    head = 0; tail = 8
    num = float('inf')
    while num > 0:
        for a in range(1, 6):
            num = dequeue()
            enqueue(num - a)
    print(Q)