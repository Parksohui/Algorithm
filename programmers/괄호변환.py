def isbalance(p):  # 균형잡인 괄호 문자열: u,v
    u, v = [], []
    for i in range(1, len(p) + 1):
        if p[:i].count("(") == p[:i].count(")"):
            u = p[:i]
            v = p[i:]
            break
    return u, v

def isright(x):  # 올바른 괄호 문자열
    stack = []
    result = True
    for i in x:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                result = False
    return result

def recur(p):
    answer = ''
    if len(p) != 0:  # 입력이 빈 문자열이 아닌 경우
        u, v = isbalance(p)  # 균형잡힌 괄호 문자열 u,v로 분리
        if isright(u) == True:  # u가 올바른 괄호 문자열이라면
            answer += u
            if len(v) != 0:
                answer += recur(v)
        else:  # u가 올바른 괄호 문자열이 아니라면
            answer = '(' + recur(v) + ')'
            x = u[1:len(u) - 1]  # 첫번째와 마지막 문자 제거
            for i in x:  # 나머지 문자열의 괄호 방향을 뒤집어서 붙이기
                if i == '(':
                    answer += ')'
                else:
                    answer += '('
    return answer


def solution(p):
    answer = ''
    answer = recur(p)

    return answer