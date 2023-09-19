N = int(input())
cnt = 0

def backtrack(nsum):
    global cnt
    if nsum == N:
        cnt += 1
        return
    
    if nsum > N:
        return
    
    for i in range(1, 4):
        nsum += i
        backtrack(nsum)
        nsum -= i

backtrack(0)
print(cnt)