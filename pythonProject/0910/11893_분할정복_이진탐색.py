def binary_search(left, right, ex_dir, target):
    global cnt

    if left > right:
        return
    
    # 타겟 숫자를 찾은 경우
    mid = (left + right) // 2
    if arr[mid] == target:
        cnt += 1
        return
    
    # 중간값보다 찾는 숫자가 큰지 작은지에 따라 오른쪽 or 왼쪽 배열 선택
    if arr[mid] < target:
        if ex_dir == 1:     # 서로 번갈아가며 선택하지 않은 경우
            return
        binary_search(mid + 1, right, 1, target)
    else:
        if ex_dir == -1:    # 서로 번갈아가며 선택하지 않은 경우
            return
        binary_search(left, mid - 1, -1, target)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N: 이진 탐색할 배열의 길이, M: 타겟 숫자들의 수
    arr = list(map(int, input().split()))   # arr: 이진 탐색할 배열
    target_list = list(map(int, input().split()))   # target_list: 타겟 숫자들의 배열

    arr.sort()
    cnt = 0
    
    for t in target_list:
        binary_search(0, N-1, 0, t)


    print(f"#{tc} {cnt}")