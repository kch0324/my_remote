T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # N: 방의 수
    arr = [0] * 201     # arr: 복도의 번호 카운팅 배열
    for i in range(N):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start
        start = (start + 1) // 2
        end = (end + 1) // 2
        for j in range(start, end + 1):
            arr[j] += 1
    print(f"#{tc} {max(arr)}")