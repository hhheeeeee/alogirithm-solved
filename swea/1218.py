import sys
sys.stdin = open('../../test.txt')
input = sys.stdin.readline

for tc in range(1, 11):
    length = int(input())
    arr = list(input().strip())
    stack = []
    result = 1

    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}

    for char in arr:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                result = 0
                break
    if stack:
        result = 0
    print(f'#{tc} {result}')

###############################
for tc in range(1, 11):
    length = int(input())
    arr = list(input().strip())
    stack = []
    result = 1
    while arr:
        if arr[0] == "(" or arr[0] == "[" or arr[0] == "{" or arr[0] == "<":
            stack.append(arr[0])
            arr.pop(0)
        elif arr[0] == ")":
            if stack and stack[-1] == "(":
                arr.pop(0)
                stack.pop()
            else:
                result = 0
                break
        elif arr[0] == "]":
            if stack and stack[-1] == "[":
                arr.pop(0)
                stack.pop()
            else:
                result = 0
                break
        elif arr[0] == "}":
            if stack and stack[-1] == "{":
                arr.pop(0)
                stack.pop()
            else:
                result = 0
                break
        elif arr[0] == ">":
            if stack and stack[-1] == "<":
                arr.pop(0)
                stack.pop()
            else:
                result = 0
                break
    if stack:
        result = 0
    print(f'#{tc} {result}')