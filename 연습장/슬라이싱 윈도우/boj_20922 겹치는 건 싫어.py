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