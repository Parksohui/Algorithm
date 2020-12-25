def solution(n):
    answer = []
    temp=str(n)
    temp=temp[::-1]
    for i in range(len(temp)):
        answer.append(int(temp[i]))
    return answer