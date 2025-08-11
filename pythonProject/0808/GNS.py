T = int(input())
for _ in range(1, T+1):
    tc, N = map(str, input().split())
    test_num = list(map(str, input().split()))
    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    count_list = []     # 빈 카운트리스트 생성
    for i in num_list:      # ZRO부터 순회하면서 test_num에 있는 숫자들을 count_list에 순서대로 추가
        for j in test_num:
            if i == j:
                count_list.append(i)
    print(f"{tc}")
    print(f"{' '.join(count_list)}")
