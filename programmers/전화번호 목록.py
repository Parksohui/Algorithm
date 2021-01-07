def solution(phone_book):
    answer = True

    for i in phone_book:
        count = 0
        for j in phone_book:
            j = j[0:len(i)]  # 접두어 찾는 경우이므로 앞 부분만 따로 저장
            count += j.count(i)
        if (count > 1):  # 접두어 존재하는 경우
            answer = False
            break

    return answer