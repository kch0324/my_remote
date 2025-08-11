def binarySearch(N, key):
    start = 1
    end = N
    cnt = 0
    while start <= end:
        cnt += 1
        middle = int((start + end) / 2)
        if middle == key:
            return cnt
        elif middle > key:
            end = middle
        else:
            start = middle
    return 1000

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    if binarySearch(P, Pa) == binarySearch(P, Pb):
        print(f"#{tc} 0")
    elif binarySearch(P, Pa) < binarySearch(P, Pb):
        print(f"#{tc} A")
    elif binarySearch(P, Pa) > binarySearch(P, Pb):
        print(f"#{tc} B")


