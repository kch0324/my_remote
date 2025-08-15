dy = [1, 0, 1, -1] # 아래, 오른쪽, 오른쪽 아래 대각선, 왼쪽 아래 대각선
dx = [0, 1, 1, 1]

def is_omok():

    for y in range(n):
        for x in range(n):
            if arr[y][x] == 'o':
                for i in range(4): # 4방향
                    ny, nx = y, x
                    cnt = 0

                    while 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 'o':
                        cnt += 1
                        ny += dy[i]
                        nx += dx[i]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [input() for _ in range(n)] # 왜 map 함수 안썼을까? map함수의 역할 : 정수로 바꿔주는 역할

    result = is_omok()
    print(f'#{tc} {result}')