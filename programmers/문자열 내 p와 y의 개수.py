def solution(s):
    pcount = s.count("p")
    pcount += s.count("P")

    ycount = s.count("y")
    ycount += s.count("Y")

    answer = True

    if (pcount != ycount):
        answer = False

    return answer