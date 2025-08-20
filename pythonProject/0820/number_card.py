def enqueue(item):
    global tail
    if (tail + 1) % (N + 1) == head:
        return
    tail = (tail + 1) % (N + 1)
    Q[tail] = item

def dequeue():
    global head
    if head == tail:
        return
    head = (head + 1) % (N + 1)
    return Q[head]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Q = [item for item in range(N + 1)]   # [0, 1, 2, 3, ... , N-1, N] 원형 큐 (0은 안채우는 칸)
    head = 0; tail = N
    i = 1
    while i < N:
        dequeue()
        num = dequeue()
        enqueue(num)
        i += 1
    print(f"#{tc} {num}")