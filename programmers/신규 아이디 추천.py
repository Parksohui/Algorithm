def solution(new_id):
    answer = ''

    new_id = new_id.lower()  # 1단계

    new_id = list(new_id)  # list로 변환

    i = 0
    while (i < len(new_id)):  # 2단계
        x = new_id[i]
        if (x.isalpha() or x.isdigit() or x == '-' or x == '_' or x == '.'):
            i += 1
            pass
        else:
            del new_id[i]

    i = 0
    if (len(new_id) != 0):
        while (i < len(new_id) - 1):  # 3단계
            if (new_id[i] == "." and new_id[i] == new_id[i + 1]):
                del new_id[i + 1]
            else:
                i += 1

    # 4단계
    if (len(new_id) != 0):
        if (new_id[0] == '.'):
            del new_id[0]
    if (len(new_id) != 0):
        if (new_id[-1] == '.'):
            del new_id[-1]

    # 5단계
    if (len(new_id) == 0):
        new_id.append("a")

    # 6단계
    if (len(new_id) >= 16):
        new_id = new_id[:15]
        if (new_id[-1] == '.'):
            del new_id[-1]

    # 7단계
    while (len(new_id) <= 2):
        new_id.append(new_id[-1])

    answer = ''.join(new_id)
    return answer