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