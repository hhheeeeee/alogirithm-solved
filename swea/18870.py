def backtrack1(cnt):
    if cnt == N:
        print(*path)
        return
    
    for i in range(1, 7):
        path.append(i)
        backtrack1(cnt + 1)
        path.pop()

def backtrack2(cnt, start):
    if cnt == N:
        print(*path)
        return
    
    for i in range(start, 7):
        path.append(i)
        backtrack2(cnt + 1, i)
        path.pop()

def backtrack3(cnt, start):
    if cnt == N:
        print(*path)
        return
    
    for i in range(start, 7):
        path.append(i)
        backtrack3(cnt+1, i+1)
        path.pop()


N, M = map(int, input().split())
path = []
if M == 1:
    # N번 던져서 나올 수 있는 모든 경우
    backtrack1(0)
    pass
elif M == 2:
    # N번 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
    backtrack2(0, 1)
else:
    # 주사위를 N번 던져서 모두 다른 수가 나올 수 있는 모든 경우
    backtrack3(0, 1)