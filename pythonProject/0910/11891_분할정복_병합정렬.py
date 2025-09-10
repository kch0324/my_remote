# 1. 분할 2. 정복 3. 병합(정렬)

def merge_sort(arr):
    global cnt
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_arr = merge_sort(left)
    right_arr = merge_sort(right)
    # 왼쪽 리스트의 마지막 요소가 오른쪽 리스트의 마지막 요소보다 크다면
    if left_arr[-1] > right_arr[-1]:
        cnt += 1

    result = merge(left_arr, right_arr)
    return result

def merge(left, right):
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    
    if l <= len(left):
        result.extend(left[l:])
    if r <= len(right):
        result.extend(right[r:])
    return result



T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # N: 정수의 개수
    arr = list(map(int, input().split()))   # arr: 정수들의 배열
    cnt = 0

    arr = merge_sort(arr)
    mid = arr[N//2]
    print(f"#{tc} {mid} {cnt}")