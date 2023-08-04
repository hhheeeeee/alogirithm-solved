import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

for tc in range(1,11):
    dump = int(input())
    box = list(map(int, input().split()))
    for i in range(dump):
        max_idx = box.index(max(box))
        min_idx = box.index(min(box))
        box[max_idx] -= 1
        box[min_idx] += 1
    print(f'#{tc} {max(box)-min(box)}')

    #print(f'#{tc} {D/(A+B)*F:.10f}')
    
    