# 4방향 대각선 델타 / 포인터로 이전에 온방향에 따라 다음에 갈수있는 방향 제어
# 범위를 벗어나면 continue -> 모든 델타에 갈곳이 없다면 return
# 내려가면서 도는방향만 생각


# 가지치기 : 모든 디저트의 종류를 set에 담아둔 뒤 현재 방문한 디저트들이 이미 set만큼이면 가지치기
 

T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # N: NxN 한변의 길이'
    # arr: 디저트 값이 저장된 2차원배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 4방향 델타: [좌하, 우하, 우상, 좌상]
    Dy = [1, 1, -1, -1]
    Dx = [-1, 1, 1, -1]

    max_v = -1
    visited = set() # 첫번째 방문카페의 좌표를 저장할 visited

    # depth: 방문한 카페수, 좌표, pointer: 그 전 왔던 방향
    def recur(depth, y, x, pointer):
        global max_v
        # 시작점인 첫번째 카페의 좌표를 저장
        if depth == 0:
            visited.add((y, x))
        # 첫번째 카페로 돌아왔으면 디저트 개수 최댓값 갱신 후 리턴
        if (y, x) in visited:
            max_v = max(max_v, depth + 1)
            return
        # 같은 숫자를 만나면 return
        if arr[y][x] in path:
            return

        path.append(arr[y][x])
        
        
        if pointer == 1:    # 좌하 -> 좌하/우하 가능
            for i in range(2):
                Ny = y + Dy[i]
                Nx = x + Dx[i]
                if Ny < 0 or Ny >= N or Nx < 0 or Nx >= N:
                    continue
                if i == 0:  # 좌하로 갈거면
                    recur(depth + 1, Ny, Nx, pointer)
                else:   # 우하로 갈거면
                    recur(depth + 1, Ny, Nx, 2)

        if pointer == 2:    # 우하 -> 우하/우상 가능
            for i in range(1,3):
                Ny = y + Dy[i]
                Nx = x + Dx[i]
                if Ny < 0 or Ny >= N or Nx < 0 or Nx >= N:
                    continue
                if i == 0:  # 우하로 갈거면
                    recur(depth + 1, Ny, Nx, pointer)
                else:   # 우상으로 갈거면
                    recur(depth + 1, Ny, Nx, 3)

        if pointer == 3:    # 우상 -> 우상/좌상 가능
            for i in range(2,4):
                Ny = y + Dy[i]
                Nx = x + Dx[i]
                if Ny < 0 or Ny >= N or Nx < 0 or Nx >= N:
                    continue
                if i == 0:  # 우상으로 갈거면
                    recur(depth + 1, Ny, Nx, pointer)
                else:   # 좌상으로 갈거면
                    recur(depth + 1, Ny, Nx, 4)

        if pointer == 4:    # 좌상 -> 좌상만 가능
            for i in range(3,4):
                Ny = y + Dy[i]
                Nx = x + Dx[i]
                if Ny < 0 or Ny >= N or Nx < 0 or Nx >= N:
                    continue
                recur(depth + 1, Ny, Nx, pointer)

    
    for i in range(N):
        for j in range(N):
            path = []
            recur(0, i, j, 1)
    
    print(f"#{tc} {max_v}")