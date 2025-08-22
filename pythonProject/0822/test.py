

def tree_traverse(g[i]):
    if i not in children.keys():
        return
    tree_traverse(L(v))
    print(v, end=' ')
    tree_traverse(R(v))


children = [0] * (V + 1) # [0, 0, 0, 0, 0 ..., 0] 0번부터~ V번 인덱스

children = {u1: [v1, v2]}
arr = [u1, v1, u1, v2 ...]
for i in range(0, len(arr), 2):
    u, v = arr[i], arr[i+1]
    children.setdefault(u1, []).append(v2)

    




