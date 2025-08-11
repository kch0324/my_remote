T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    max_c = 0
    temp_c = 0
    for i in range(N):
        if arr[i] == 1:
            temp_c += 1
            if max_c < temp_c:
                max_c = temp_c
        else:
            temp_c = 0
    print(f"#{tc} {max_c}")
            
