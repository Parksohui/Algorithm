def solution(citations):
    answer = 0

    citations.sort(reverse=True)

    if min(citations) >= len(citations):
        answer = len(citations)
    else:
        for i in range(max(citations)):
            if citations[i] <= i:
                answer = i
                return answer

    return answer