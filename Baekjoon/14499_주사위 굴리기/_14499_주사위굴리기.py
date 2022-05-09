import sys

def throw_dice(a,b,c,d,e,f):
    temp = [0, 0, 0, 0, 0, 0]
    temp[0] = dice[a]
    temp[1] = dice[b]
    temp[2] = dice[c]
    temp[3] = dice[d]
    temp[4] = dice[e]
    temp[5] = dice[f]
    return temp

if __name__=='__main__':
    n,m,x,y,k=map(int,sys.stdin.readline().split()) # 세로, 가로, 주사위 좌표, 명령 개수

    arr=[] # 지도
    for i in range(n):
        arr.append(list(map(int,sys.stdin.readline().split())))

    command=list(map(int,sys.stdin.readline().split())) # 명령

    dice=[0,0,0,0,0,0] # 주사위

    for i in command:
        flag=False
        if i==1: # 동
            if y+1<m:
                y+=1
                flag=True
                dice = throw_dice(0, 4, 2, 5, 3, 1)
        elif i==2: # 서
            if y-1>=0:
                y-=1
                flag = True
                dice = throw_dice(0, 5, 2, 4, 1, 3)
        elif i==3: # 북
            if x-1>=0:
                x-=1
                flag = True
                dice = throw_dice(1, 2, 3, 0, 4, 5)
        elif i==4: # 남
            if x+1<n:
                x+=1
                flag = True
                dice = throw_dice(3, 0, 1, 2, 4, 5)
        if flag==True:
            if arr[x][y] == 0: # 이동한 칸에 쓰여있는 수가 0
                arr[x][y] = dice[3]
            else: # 0이 아닌 경우
                dice[3] = arr[x][y]
                arr[x][y]=0
            print(dice[1])