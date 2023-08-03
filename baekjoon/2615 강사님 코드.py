import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

def gumsa(y, x, color):
    dy = [-1, 0, 1, -1]
    dx = [0, -1, 1, 1]
    used = [[0]*19 for _ in range(19)]
    for i in range(4):
        used = [[0]*19 for _ in range(19)]
        new_y = y
        new_x = x
        count = 1
        coords = []
        coords.append((y+1, x+1))
        while True:
            new_y += dy[i]
            new_x += dx[i]
            
            if new_y < 0 or new_x < 0 or new_y >= 19 or new_x >= 19:
                break
            if grid[new_y][new_x] != color:
                break
            if used[new_y][new_x] == 1:
                break
            used[new_y][new_x] = 1

            count += 1
            coords.append((new_y+1, new_x+1))
            if count > 5:
                return False, coords
        new_y = y
        new_x = x
        
        while True:
            new_y -= dy[i]
            new_x -= dx[i]
            
            if new_y < 0 or new_x < 0 or new_y >= 19 or new_x >= 19:
                break
            if grid[new_y][new_x] != color:
                break
            if used[new_y][new_x] == 1:
                break

            used[new_y][new_x] = 1

            count += 1
            coords.append((new_y+1, new_x+1))
            if count > 5:
                return False, coords

        if count == 5:
            return True, coords
            
    return False, coords

def run_gumsas():
    for y in range(19):
        for x in range(19):
            color = grid[y][x]
            if color == 0:
                continue
            win_bool, coords= gumsa(y, x, color)
            if win_bool:
                for find_x in range(19):
                    for find_y in range(19):
                        if (find_y, find_x) in coords:
                            return color, find_y, find_x
    return -1, -1, -1


grid = [list(map(int, input().split())) for _ in range(19)]
win_color, min_y, min_x = run_gumsas()
if win_color == -1:
    print(0)
else:
    print(win_color)
    print(min_y, min_x)