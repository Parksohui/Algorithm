import sys #입력 시간 단축을 위해 sys사용

if __name__=='__main__' :
    temp=list(sys.stdin.readline().strip()) #초기 편집기에 입력되어있는 문자열 입력

    turn=int(input()) #명령어 수 입력

    temp2=[] #커서 기준 오른쪽 list

    for i in range(turn): #명령어 입력
        task=sys.stdin.readline().split()
        if len(temp)!=0 and task[0]=='L': #커서 왼쪽으로 옮김
            temp2.append(temp.pop())
        elif len(temp2)!=0 and task[0]=='D': #커서 오른쪽으로 옮김
            temp.append(temp2.pop())
        elif task[0]=='B': #커서 왼쪽에 있는 문자 삭제
            if len(temp)!=0:
                temp.pop()
        elif task[0]=='P': #문자를 커서 왼쪽에 추가
            temp.append(task[1])

    temp2.reverse()


    print(''.join(temp)+''.join(temp2))