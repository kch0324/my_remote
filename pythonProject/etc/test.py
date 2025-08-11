T = int(input())

for tc in range (1,T+1):
    arr = [list(map(int, input().split())) for _ in range(100)]

    lst = []
    left = 0
    right = 0
    for cr in range(100):
        left += arr[cr][cr]
        right += arr[cr][99-cr]

    lst.append(left)
    lst.append(right)

    for i in range(100):
        hag = 0
        ten = 0
        for j in range(100):
            hag += arr[i][j]
            ten += arr[j][i]
        lst.append(hag)
        lst.append(ten)

    mx = 0
    for re in range (len(lst)):
        if lst[re] >= mx:
            mx = arr[re]

    print(f"#{tc} {mx}")