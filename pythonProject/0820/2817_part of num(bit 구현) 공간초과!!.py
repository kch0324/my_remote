T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())    # N: 숫자의 개수 (1<= N <= 20), K: 숫자들의 합이 되어야 하는 수 (1 <= K <= 1000)
    arr = list(map(int, input().split()))   # arr: 숫자들의 배열
    
    bit = [0] * N
    bit_list = []

    def get_bit(bit, i, N): # bit, 인덱스 시작점 i, 끝낼 범위 N을 매개변수로 받음
        global bit_list
        if i == N:
            bit_list.append(bit[:])
            return
        for j in range(2):
            bit[i] = j
            get_bit(bit, i + 1, N)
    
    get_bit(bit, 0, N)

    cnt = 0
    for bit in bit_list:
        sums = 0    # 해당 부분집합의 합
        for idx in range(N):   # bit를 순회하며 0,1을 조회
            if bit[idx]:   #  해당 숫자가 부분집합에 있으면 arr 해당 인덱스 요소를 합에 더함
                sums += arr[idx]
        if sums == K:
            cnt += 1
    
    print(f"#{tc} {cnt}")