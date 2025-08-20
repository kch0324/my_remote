# 겹치는 건 싫어

N, K = map(int, input().split())
arr = list(map(int, input().split()))
l = 0
max_length = 0

# 카운팅 배열
count_arr = [0] * 100000

for r in range(N):
    count_arr[arr[r]] += 1
    while K + 1 in count_arr:
        count_arr[arr[l]] -= 1
        l += 1
    max_length = max(max_length, r - l + 1)

print(max_length)

##################################################################################

N, K = map(int, input().split())
lst = list(map(int, input().split()))

# 같은 원소가 K개 이하로 들어 있는 최장 수열의 길이
temp = {}
left = length = 0

for right in range(N):
    if lst[right] not in temp:
        temp[lst[right]] = 1
    else:
        temp[lst[right]] += 1

    while temp[lst[right]] > K:
        temp[lst[left]] -= 1
        left += 1

    length = max(length, right - left + 1)

print(length)