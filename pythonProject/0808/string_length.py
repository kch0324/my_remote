T = int(input())
for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())
    max_v = 0

    for i in str1:
        temp_v = 0
        for j in str2:
            if i == j:
                temp_v += 1
        if max_v < temp_v:
            max_v = temp_v
    print(f"#{tc} {max_v}")