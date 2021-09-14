def solution(info, query):
    answer = []

    val = []
    for i in info:  # info: string to list
        val.append(list(i.split()))

    qu = []
    for i in query:  # query: string to list
        x = list(i.split())
        for j in range(3):  # remove "and"
            x.remove("and")
        qu.append(x)

    for i in qu:
        result = 0  # count
        for j in val:  # - or value same: pass
            if i[0] == '-' or i[0] == j[0]:
                if i[1] == '-' or i[1] == j[1]:
                    if i[2] == '-' or i[2] == j[2]:
                        if i[3] == '-' or i[3] == j[3]:
                            if int(i[4]) <= int(j[4]):
                                result += 1
        answer.append(result)  # answer

    return answer