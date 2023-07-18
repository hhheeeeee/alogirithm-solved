import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()[:n]))
arr = sorted(list(set(num_list)))

com_dic={arr[i] : i for i in range(len(arr))}

for elem in num_list:
    print(com_dic[elem], end=' ')

# list.index(i)는 시간복잡도 O(N)
# dict[i]는 시간복잡도 O[1]