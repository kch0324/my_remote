# 슬라이싱 윈도우
# limit보다 작은 구간합의 최대 개수

arr = [1,2,3,4,5]
LIMIT = 7
l, sums = 0, 0
max_length = 0
max_sums = 0

for r in range(len(arr)):
    sums += arr[r]
    while sums > LIMIT:     # 구간합이 제한보다 커지면 발동
        sums -= arr[l]
        l += 1
    if max_length < r - l + 1:
        max_length = r - l + 1
        max_sums = sums

print(max_length)
print(max_sums)