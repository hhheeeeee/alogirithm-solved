import sys
sys.stdin = open('1.txt')

N = int(input())
arr = sorted(list(map(int, input().split())))
high = N - 1
low = 0
reslow, reshigh = 0, 0
ressum = 10e9 + 1

# -99-2 -1 4 98
while low < high:
    if arr[low] + arr[high] == 0:
        reslow = arr[low]
        reshigh = arr[high]
        break

    if abs(arr[low] + arr[high]) < abs(ressum):
        reslow = arr[low]
        reshigh = arr[high]
        ressum = arr[low] + arr[high]

    if arr[low] + arr[high] > 0:
        high -= 1
    elif arr[low] + arr[high] < 0:
        low += 1


print(reslow, reshigh)

'''
4
0 0 5 5

0 0

4
999999995 999999996 999999997 1000000000
999999995 999999996
'''