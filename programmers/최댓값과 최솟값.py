def solution(s):
    answer = ''
    temp=[]
    temp=s.split() #공백 기준 list
    temp = list(map(int, temp)) #str to int

    answer+=str(min(temp)) #min
    answer+=" "
    answer+=str(max(temp)) #max

    return answer