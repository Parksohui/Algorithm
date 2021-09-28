def solution(msg):
    answer = []

    # 사전 초기화
    dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
            'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
            'Z': 26}

    i = 0
    idx = 27
    while i < len(msg):
        for j in range(i + 1, len(msg) + 1):
            if msg[i:j] in dict:  # 사전에 있는 값이면
                if j == len(msg):  # 마지막 값이면
                    answer.append(dict[msg[i:j]])
                    i = j
                pass
            else:  # 사전에 없으면
                answer.append(dict[msg[i:j - 1]])  # 색인 번호 추가
                dict[msg[i:j]] = idx  # 단어 사전에 등록
                idx += 1
                i = j - 1
                break
    return answer