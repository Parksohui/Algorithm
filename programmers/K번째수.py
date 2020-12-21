def solution(array, commands):
    arraytemp=[]
    answer=[]
    for i in range(len(commands)):
        arraytemp=array[commands[i][0]-1: commands[i][1]]
        arraytemp.sort()
        answer.append(arraytemp[commands[i][2]-1])
    return answer