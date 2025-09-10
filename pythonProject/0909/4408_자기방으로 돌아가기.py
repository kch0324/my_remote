T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    students = []
    for i in range(N):
        start_room, end_room = map(int, input().split())
        if start_room > end_room:   # 시작방이 더 크면 오름차순으로 바꿔줌
            start_room, end_room = end_room, start_room
            # 해당 시작방에서 끝방으로 이동할때 지나게 되는 복도의 번호를 계산
        start_hallway = (start_room + 1) // 2
        end_hallway = (end_room + 1) // 2
        students.append((start_hallway, end_hallway))
    students.sort(key=lambda x: x[1])

    cnt = 0
    while students:
        end = students[0][1]
        students.pop(0)
        cnt += 1
        i = 0
        while i < len(students):   # 배열 마지막요소까지 순회
            start = students[i][0]
            if start > end: # 다음 학생의 start가 이전 학생의 end보다 크면 동시에 가능
                end = students[i][1]
                students.pop(i)
            else:   # 동시에 못가면 다음번 학생 탐색
                i += 1

    print(f"#{tc} {cnt}")