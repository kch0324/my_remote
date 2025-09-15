def make_set(n):
    # 1 ~ n 까지의 원소가 "각자 자기 자신이 대표자라고 설정"
    leaders = [i for i in range(n + 1)]
    return leaders

def find_set(x):
    if x == leaders[x]:  # 자기 자신이 대표라면(대표자를 찾았다면) 반환
        return x
    leaders[x] = find_set(leaders[x])  # 경로 압축
    return leaders[x]

def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:  # 같은 조면 리턴
        return
    
    leaders[rep_x] = rep_y


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    leaders = make_set(N)
    arr = list(map(int, input().split()))
    # 유니온파인드로 조를 구성
    for i in range(M):
        union(arr[2*i], arr[2*i + 1])
    
    # 모든 원소의 대표자를 최신화
    for i in range(1, N + 1):
        find_set(i)

    check = set(leaders)    # 중복되지 않는 대표자의 수가 조의 개수
    print(f"#{tc} {len(check)-1}")   # 대표자 수에서 0은 제거