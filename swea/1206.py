import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

def view(buildings, n):
    direction  = [-2, -1 , 1, 2]
    cnt = 0

    for idx in range(2,n-2):
        side_buildings = []
        for dir in direction:
            side_buildings.append(buildings[idx] - buildings[idx + dir])
        cnt += max(0, min(side_buildings))         
    
    return cnt


for testcase in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))
    answer = view(buildings, n)
    print(f"#{testcase} {answer}")