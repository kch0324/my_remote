# def solution(i):
#     global path
#     if i > N:
#         print(path)
#         return
#     for j in range(1, 4):
#         path.append(j)
#         solution(i + 1)
#         path.pop()
#
# N = int(input())
# path = []
# solution(0)


def Main():
    KFC(0)
    print('끝')

def KFC(x):
    print(x)
    if x == 994:
        return
    KFC(x + 1)

Main()