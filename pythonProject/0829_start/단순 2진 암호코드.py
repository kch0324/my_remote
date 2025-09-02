# 행우선 순회 : 뒤부터 순회해서 1이 나오면 해당 좌표(j) - 55 가 암호코드 시작 좌표(j)
# 시작 좌표부터 56번 j를 순회 (7번씩 8번) 해당하는 코드를 딕셔너리에서 찾아서 리스트에 저장
pw_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
            '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]   # 각 행이 문자열인 NxM 리스트

    def find_code(arr, N, M):
        for i in range(N):
            for j in range(M-1, -1, -1):    # 뒤부터 탐색
                if arr[i][j] == '1':
                    return (i, j - 55)  # 암호 시작 좌표 반환

    i, j = find_code(arr, N, M)
    pw = []
    code = ''
    for c in range(j, j + 56):
        code += arr[i][c]
        if len(code) == 7:
            pw.append(pw_dict[code]) # 코드가 만들어질때마다 해석한 숫자를 pw에 담고, 코드 초기화
            code = ''

    pw = [0] + pw   # 인덱스로 접근하기 위해 0번부터 시작
    odd = 0; even = 0
    for i in range(1, 9):
        if i % 2 == 1:
            odd += pw[i]
        else:
            even += pw[i]

    if (odd * 3 + even) % 10 == 0:  # 올바른 코드
        result = odd + even
    else:   # 올바르지 않은 코드
        result = 0

    print(f"#{tc} {result}")