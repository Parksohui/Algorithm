def solution(files):
    answer = []
    temp = []

    for i in files:
        head, num, tail = '', '', ''
        check = False
        numcheck = False
        for j in i:
            if not j.isdigit():
                if check == True:  # Tail
                    tail += j
                    numcheck = True
                else:  # HEAD
                    head += j
            elif j.isdigit():
                if numcheck == True:  # Tail
                    tail += j
                else:  # NUMBER
                    num += j
                    check = True
                    if len(num) >= 5:  # NUMBER 한글자 ~ 최대 다섯 글자
                        numcheck = True
        temp.append([head, num, tail])

    temp.sort(key=lambda x: (x[0].upper(), int(x[1])))  # 정렬) 1. HEAD 기준 2. NUMBER 기준 3. 입력 순서

    for i in temp:
        answer.append(''.join(i))

    return answer

# abc123defg123 의 경우 NUMBER과 TAIL 구분 확실히 해주어야 통과