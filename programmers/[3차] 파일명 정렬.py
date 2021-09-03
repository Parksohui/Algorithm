def solution(files):
    answer = []

    temp = []
    for i in files:
        head, num, tail = '', '', ''
        check = False
        for j in i:
            if not j.isdigit() and check == False:  # HEAD
                head += j
            elif j.isdigit():  # NUMBER
                num += j
                check = True
            else:  # TAIL
                if check == True:
                    tail += j

        temp.append([head, num, tail])

    temp.sort(key=lambda x: (x[0].upper(), int(x[1])))  # 정렬) 1. HEAD 기준 2. NUMBER 기준 3. 입력 순서

    for i in temp:
        answer.append(''.join(i))

    return answer