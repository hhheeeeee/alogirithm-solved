import heapq

N = int(input())
arr = list(map(int, input().split()))
que = [] # 황금과 짱돌을 저장할 최소 힙
cnt = 0
for i in range(N): # 입력받은 황금의 무게를 최소 힙에 추가
    heapq.heappush(que, [arr[i], -1]) # 각 황금의 무게와 -1(황금 의미)를 저장

while que: # 힙에 요소가 있을 때까지 반복
    x, tp = heapq.heappop(que) # 힙에서 가장 가까운 돌을 꺼낸다
    if tp == 0: # 꺼낸 돌이 짱돌이면
        break
    cnt += 1

    y, tp = heapq.heappop(que) # 다음 가장 가벼운 돌을 꺼낸다
    if tp == 0: #꺼낸 돌이 짱돌이면
        break
    else: # 꺼낸 돌이 황금이면
        heapq.heappush(que, [y+2, 0]) # 황금 2개 무게를의 짱돌을 힙에 추가
    cnt += 1

print(cnt)

