def castle(depth):
    global cnt
    if depth == N:
        cnt += 1
        return
    
    for i in range(N):
        if i not in arr:
            arr.append(i)
            castle(depth + 1)
            arr.pop()


N = int(input())
cnt = 0
arr = []
castle(0)
print(cnt)