def solution(s):
    answer = 0

    for i in range(len(s)):
        stack = []
        check = True
        for j in s:  # 올바른 괄호인지 판별
            if j == '[' or j == '(' or j == '{':  # 왼쪽 괄호 _ 추가
                stack.append(j)
            elif j == ']':  # 각 짝에 맞는 괄호일 경우 제거, 아니면 check=False
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    check = False
            elif j == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    check = False
            else:
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    check = False
        if check == True and len(stack) == 0:  # 올바른 괄호라면
            answer += 1

        s = s[1:] + s[0]  # s를 왼쪽으로 x칸만큼 회전

    return answer