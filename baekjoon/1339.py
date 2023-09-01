import sys
sys.stdin = open('../1.txt')

from collections import deque

N = int(input())
arr = []
alphabet = dict()
for _ in range(N):
    arr.append(input())

for word in arr:
    digit = 1
    for j in range(len(word) - 1, -1, -1):
        char = word[j]
        if char not in alphabet.keys():
            alphabet[char] = digit
        else:
            alphabet[char] += digit
        digit *= 10

# print(alphabet)
sorted_alpha = sorted(alphabet.items(), key = lambda x : x[1], reverse = True)
alphanum = dict()
number = [0,1,2,3,4,5,6,7,8,9]
for key, value in sorted_alpha:
    alphanum[key] = number.pop()

changed_num = []
for word in arr:
    num = ""
    for c in word:
        num += str(alphanum[c])
    changed_num.append(int(num))

# print(changed_num)
print(sum(changed_num))

'''
AB
BC
CD
DE
EF
384 [56, 67, 78, 89, 94]

2
AB
BB

4
ABCD
BCDA
CDAB
DABG

33329


10
ABB
BC
BC
BC
BC
BC
BC
BC
BC
BC
1772
'''