def DFS(i, sums):   # i: 부분집합 bit 인덱스, sums: 부분집합의 합
    global cnt
    if i == N:  # 마지막 부분집합까지 도달하면 sums 확인 후 탈출
        if sums == K:
            cnt += 1
        return
    DFS(i+1, sums)  # bit[i] == 0인경우
    DFS(i+1, sums + arr[i])  # bit[i] == 1인경우

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())    # N: 숫자의 개수 (1<= N <= 20), K: 숫자들의 합이 되어야 하는 수 (1 <= K <= 1000)
    arr = list(map(int, input().split()))   # arr: 숫자들의 배열
    
    cnt = 0    
    DFS(0, 0)
    
    print(f"#{tc} {cnt}")