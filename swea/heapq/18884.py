import heapq
score = [500]
for i in range(1, int(input())+1):
    a, b = map(int, input().split())
    heapq.heappush(score, a)
    heapq.heappush(score, b)
    temp = []
    for _ in range(i):
        temp.append(heapq.heappop(score))
    n = heapq.heappop(score)
    print(n)
    heapq.heappush(score, n)
    for i in temp:
        heapq.heappush(score, i)