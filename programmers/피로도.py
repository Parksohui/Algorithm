from itertools import permutations  # 순열

def solution(k, dungeons):
    answer = -1

    arr = list(permutations(dungeons, len(dungeons)))  # 모든 경우의 수
    for i in arr:
        start = k  # init
        cnt = 0  # count
        for j in i:
            if start >= j[0]:  # 최소 필요 피로도 충족
                start -= j[1]  # 피로도 소모
                cnt += 1  # 탐험 가능
            else:
                break
        if cnt > answer:  # 탐험할 수 있는 최대 던전 수
            answer = cnt

    return answer