import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def append_star(LEN): # 6
    if LEN == 3:
        return ['  *  ',' * * ','*****']

    Stars = append_star(LEN//2) # ['  *  ',' * * ','*****']
    L = []  
    
    for S in Stars:
        L.append(' '*(LEN // 2)+S+' '*(LEN // 2))
    for S in Stars:
        L.append(S +" "+ S)
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))