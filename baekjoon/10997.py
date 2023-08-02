import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def append_star(LEN): # 3

    if LEN == 2:
        return ["*****","*    ","* ***","* * *","* * *","*   *","*****"]

    Stars = append_star(LEN-1) # ['*']
    L = []  
    upper = '*' * (1 + 4 * (LEN - 1))
    second_u = '*'+ " " * (4 * (LEN - 1))
    second_b = '*'+ " " * ((4 * (LEN - 1)) - 1)+ "*"
    L.append(upper)
    L.append(second_u)
    L.append("* " +Stars[0]+"**")
    for S in Stars[1:]:
        L.append("* "+ S + " *")
    L.append(second_b)
    L.append(upper)
    
    return L

n = int(sys.stdin.readline().strip())
if n == 1:
    print("*")
else:
    result = append_star(n)
    print('*' * (1 + 4 * (n - 1)))
    print("*")
    print(*result[2:], sep = '\n')