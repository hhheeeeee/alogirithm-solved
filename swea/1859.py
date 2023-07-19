#import sys
#sys.stdin = open('test.txt')
#input = sys.stdin.readline

T = int(input())
for testcase in range(1, T+1):
    M = int(input()) #배열의 길이 (안쓰임)
    answer = 0 #출력할 정답
    arr = list(map(int, input().split())) #배열 입력 받기
    sellPrice = 0 #현재 판매가격(최댓값)
    for val in arr[::-1]: # 배열 거꾸로 순회
        if val >= sellPrice: #현재 값이 최댓값보다 크거나 같다면
            sellPrice = val #최댓값 업데이트
        else:
            answer += sellPrice - val #아니라면 정답값에 가격차이를 더한다. (현재 값에 구매해서 최댓값에 판다)
    print(f"#{testcase} {answer}")