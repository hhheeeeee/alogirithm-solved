import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

room = input()
nums = [0] * 10

for num in room:
    nums[int(num)] += 1

nums[6] = (nums[6] + nums[9] + 1) // 2
nums[9] = 0

print(max(nums))

# 반례:
# 161666
# 2

# 666999
# 3

# 6669999
# 4

# 999998
# 3