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

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    N += 1
    Q = [0] + arr   # 원형큐에 요소를 다 넣은 상태
    head = 0; tail = N - 1

    i = 1
    while i <= M + 1:    # M번 이동 후 가장 앞에 있는 숫자는 M+1번째에 dequeue 한 숫자
        num = dequeue()
        enqueue(num)
        i += 1
    print(f"#{tc} {num}")