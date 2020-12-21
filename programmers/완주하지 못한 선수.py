def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)

    return participant[0]