import sys
sys.stdin = open('../1.txt')
from collections import deque

for tc in range(1, int(input()) + 1):
    cards = {'S' : [], 'D' : [], 'H': [], 'C' : [] }
    line = input()
    res = 1
    for i in range(0, len(line), 3):
        Deck = line[i]
        num = line[i + 1] + line[i + 2]
        if int(num) in cards[Deck]:
            res = 0
            break
        else:
            cards[Deck].append(int(num))
    print(f'#{tc} ', end = "")
    if res:
        for key, values in cards.items():
            print(13 - len(set(values)), end = " ")
        print()
    else:
        print('ERROR')