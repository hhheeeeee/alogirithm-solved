import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def append_star(LEN): # 3
    if LEN == 1:
        return ['*']

    Stars = append_star(LEN-1) # ['*']
    L = []  
    upper = '*' * (1 + 4 * (LEN - 1))
    second = '*'+ " " * ((4 * (LEN - 1)) - 1)+ "*"
    L.append(upper)
    L.append(second)
    for S in Stars:
        L.append("* "+ S + " *")
    L.append(second)
    L.append(upper)
    
    return L

n = int(sys.stdin.readline().strip())
result = append_star(n)
print(*result, sep = '\n')


# n = 3  3×2k, k = 0
# aa*aa                        
# a* *                       
# ***** 

# n = 6  3×2k, k = 1  
# aaaaa*                        
#     * *                       
#    *****                      
#   *     *                     
#  * *   * *                    
# ***** ***** 