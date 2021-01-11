
def solution(n):
    answer = 0

    result =[]
    result.append(0)
    result.append(1)

    for i in range(2 , n +1):  # list의 앞 두개를 더해서 만들어냄
        result.append(result[ i -1 ] +result[ i -2 ])

    answer =result[-1] %1234567

    return answer