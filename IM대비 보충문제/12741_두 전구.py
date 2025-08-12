T = int(input())
for tc in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    dat = [0] * 101
    for i in range(A+1, B+1):
        dat[i] += 1
    for j in range(C+1, D+1):
        dat[j] += 1
    
    cnt = 0
    for p in range(101):
        if dat[p] == 2:
            cnt += 1
    
    print(f"#{tc} {cnt}")
#####################################################################################################################
T = int(input())

for tc in range(1, T + 1):
    A, B, C, D = map(int, input().split())

    X_dat = [0] * 101 # 최대값이 100이기 때문
    Y_dat = [0] * 101

    # X 전구가 켜진 시간대 dat에 기록
    for i in range(A + 1, B + 1):
        X_dat[i] = 1 # i 값을 dat의 인덱스로 썼다

    # Y 전구가 켜진 시간대 dat에 기록
    for i in range(C + 1, D + 1):
        Y_dat[i] = 1

    cnt = 0
    for i in range(101):
        if X_dat[i] == 1 and Y_dat[i] == 1: cnt += 1

    print(f'#{tc} {cnt}')