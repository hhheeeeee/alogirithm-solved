N, K = map(int, input().split())
churo = [int(input()) for _ in range(N)]
churo.sort(reverse=True) 

low = 1  
high = churo[0] 

while low <= high:
    mid = (low + high) // 2
    count = sum([c // mid for c in churo]) 

    if count >= K:
        low = mid + 1
    else: 
        high = mid - 1

print(high)