N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N):
    p, c1, c2 = map(int, input().split())
    tree[p].append(c1)
    tree[p].append(c2)

# 중위순회
def inorder(p):
    if tree[p][0] != -1:
        inorder(tree[p][0])
    print(p, end = " ")
    if tree[p][1] != -1:
        inorder(tree[p][1])

# 전위순회
def preorder(p):
    print(p, end = " ")
    if tree[p][0] != -1:
        preorder(tree[p][0])
    if tree[p][1] != -1:
        preorder(tree[p][1])

# 후위순회
def postorder(p):
    if tree[p][0] != -1:
        postorder(tree[p][0])
    if tree[p][1] != -1:
        postorder(tree[p][1])
    print(p, end = " ")


inorder(1)
print()
preorder(1)
print()
postorder(1)
