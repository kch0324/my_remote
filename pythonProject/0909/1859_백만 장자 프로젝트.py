# 1. arr에 담는다.
# 2. arr의 max를 구하고 max보다 왼쪽인것을 모두 구한다.
# 3. 왼쪽인것들 각각 max와의 차만큼 result에 더해준다.
# 4. arr에서 max까지의 요소들을 지운다.
# 5. 새로운 arr에서 다시 max를 구한다(반복) -> while arr까지

T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # 매매일 수
    arr = list(map(int, input().split()))   # arr: 매매가들의 배열

    max_v = max(arr)    # 최댓값 찾기
    idx = arr.index(max_v)  # 최댓값 인덱스
    result = 0
    while arr:
        for i in range(idx):
            result += (arr[idx] - arr[i])
        arr = arr[idx + 1: ]
        if arr:
            max_v = max(arr)    # 최댓값 다시 찾기
            idx = arr.index(max_v)  # 최댓값 인덱스
    print(f"#{tc} {result}")