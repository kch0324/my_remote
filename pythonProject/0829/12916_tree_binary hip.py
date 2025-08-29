def enq(n):     # 최소힙 삽입 함수
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = [0] * (N + 1)
    last = 0
    for i in arr:
        enq(i)

    sum_pal = 0
    p = last // 2
    while p:
        sum_pal += heap[p]
        p = p // 2

    print(f"#{tc} {sum_pal}")