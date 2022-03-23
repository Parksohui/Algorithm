import sys

if __name__=='__main__':
    N=int(input()) # 보드 크기
    k=int(input()) # 사과 개수

    graph=[[0]*N for i in range(N)]
    for i in range(k): # 사과 위치 표시
        x,y=map(int,sys.stdin.readline().split())
        graph[x-1][y-1]=1

    L=int(input()) # 뱀의 방향 변환 횟수
    info=[] 
    for i in range(L): # 뱀의 방향 변환 정보
        info.append(sys.stdin.readline().split())

    now=[[0,0]] # 뱀의 위치 기록
    D='R' # 방향
    snake=[[0]*N for i in range(N)] # 뱀
    snake[0][0]=1
    time=0 # 초
    while True:
        if len(info)!=0: # x 초 끝난 뒤 방향 회전
            if time==int(info[0][0]):
                temp=info.pop(0)
                if temp[1]=='L': # 방향 전환
                    if D=='R':
                        D='U'
                    elif D=='L':
                        D='D'
                    elif D=='U':
                        D='L'
                    else:
                        D='R'
                else:
                    if D=='R':
                        D='D'
                    elif D=='L':
                        D='U'
                    elif D=='U':
                        D='R'
                    else:
                        D='L'
        time += 1
        if D=='R': # 오른쪽
            temp=[now[-1][0], now[-1][1]+1]
        elif D=='L': # 왼쪽
            temp=[now[-1][0], now[-1][1]-1]
        elif D=='U': # 위
            temp=[now[-1][0]-1, now[-1][1]]
        else: # 아래
            temp=[now[-1][0]+1, now[-1][1]]

        if temp[0] >= 0 and temp[0] < N and temp[1] >= 0 and temp[1] < N: # 보드 범위 안이라면
            if snake[temp[0]][temp[1]] == 1: # 자기 자신의 몸과 부딪히면 게임 끝
                break
            snake[temp[0]][temp[1]] = 1 # 뱀 머리를 다음 칸에 위치
            now.append(temp) # 뱀 위치 추가

            if graph[now[-1][0]][now[-1][1]] != 1: # 사과가 없다면 몸 길이를 줄여서 꼬리가 위치한 칸을 비움
                temp = now.pop(0)
                snake[temp[0]][temp[1]] = 0
            else: # 사과가 있다면 사과가 없어지고 꼬리는 움직이지 않음
                graph[now[-1][0]][now[-1][1]]=0
        else: # 벽에 부딪히면 게임 끝
            break

    print(time)