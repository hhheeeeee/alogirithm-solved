import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def make_star(LEN): # 9
    if LEN == 1:
        return ['*']
    
    Stars = make_star(LEN // 3) #[*** * * ***]
    L = []
    for S in Stars:
        L.append(S * 3)  #***
    for S in Stars:
        L.append(S + " " * (LEN // 3) + S) #* *
    for S in Stars:    
        L.append(S * 3) #***
        
    return L

n = int(input())
result = make_star(n)
print(*result, sep = '\n')