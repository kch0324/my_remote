# 선형큐
QSIZE = 4
Q = [0] * QSIZE
head = tail = -1

def enqueue(item):
    global tail
    if tail == QSIZE - 1:
        print('full')
        return
    tail += 1
    Q[tail] = item

def dequeue():
    global head
    if head == tail:
        print('empty')
        return
    head += 1
    return Q[head]

# 원형큐
QSIZE = 4
Q = [0] * QSIZE
head = tail = 0

def enqueue(item):
    global tail
    if (tail + 1) % QSIZE == head:
        print('full')
        return
    tail = (tail + 1) % QSIZE
    Q[tail] = item

def dequeue():
    global head
    if head == tail:
        print('empty')
        return
    head = (head + 1) % QSIZE
    return Q[head]