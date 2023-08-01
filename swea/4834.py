#  가장 많은 카드의 숫자와 장 수
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    cards = input().strip()
    temp = [0] * 10
    for i in cards:
        temp[int(i)] += 1
    max_num = 0
    for i in range(10):
        if temp[i] == max(temp):
            max_num = i
    print(f'#{testcase} {max_num} {max(temp)}')


#  가장 많은 카드의 숫자와 장 수
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    cards = input()
    # 숫자의 등장 횟수를 저장할 딕셔너리 생성
    counts = {str(n) : 0 for n in range(10)}
    for card in cards:
        counts[card] += 1
    max_count = max(counts.values())
    max_number = max([int(num) for num, count in counts.items() if count == max_count])
    print(f'#{testcase} {max_number} {max(max_count)}')


