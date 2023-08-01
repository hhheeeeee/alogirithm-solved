def subset(N,K):
    cnt = 0
    arr = [i for i in range(1,13)]
    for i in range(1<<12): #만약 N = 3 이면 100 : 2^3 = 8
        result = []
        for j in range(12): # j는 0 1 2
            if i & (1<<j):
                result.append(arr[j])
        if len(result) == N and sum(result) == K:
            cnt += 1
    return cnt

T = int(input())
for testcase in range(1,T+1):
    N, K = map(int, input().split())
    print(f'#{testcase} {subset(N,K)}')
# 1 2 3 4 5