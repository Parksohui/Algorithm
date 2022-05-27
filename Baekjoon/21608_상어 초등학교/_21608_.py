import sys

def main():
    n=int(input())
    arr=[[0]*n for i in range(n)]

    info=[]
    for i in range(n*n): # 정보
        info.append(list(map(int,sys.stdin.readline().split())))

    arr[1][1]=info[0][0]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(1,n*n):
        temp=[[0]*n for i in range(n)]
        for j in range(n):
            for k in range(n):
                cnt=0
                zero_cnt=0
                if arr[j][k]==0:
                    for v in range(4): # 인접한 칸 중 좋아하는 학생, 비어있는 칸 구하기
                        x=j+dx[v]
                        y=k+dy[v]
                        if 0<=x<n and 0<=y<n :
                            if arr[x][y]!=0 and arr[x][y] in info[i]:
                                cnt+=1
                            elif arr[x][y]==0:
                                zero_cnt+=1

                temp[j][k]=[cnt,zero_cnt]
        num=-1
        zero_num=-1
        for j in range(n):
            for k in range(n):
                # 비어있는 칸 중 -> 좋아하는 학생이 인접한 칸에 가장 많은 칸
                if arr[j][k]==0 and temp[j][k][0]>=num:
                    if temp[j][k][0]>num:
                        xy = [j, k]
                        zero_num=temp[j][k][1]
                    else: # 만족하는 칸이 여러 개이면
                        # 인접한 칸 중에서 비어있는 칸이 가장 많은 칸
                        if temp[j][k][1]>zero_num:
                            xy = [j, k]
                            zero_num=temp[j][k][1]
                    num = temp[j][k][0]
        arr[xy[0]][xy[1]]=info[i][0]

    result=0 # 학생의 만족도
    for i in range(n):
        for j in range(n):
            for v in info:
                cnt = 0
                if arr[i][j]==v[0]:
                    for k in range(4): # 인접한 칸에 앉은 좋아하는 학생 수 구하기
                        x=i+dx[k]
                        y=j+dy[k]
                        if 0<=x<n and 0<=y<n:
                            if arr[x][y] in v:
                                cnt+=1
                    break
            if cnt==0 :
                result+=0
            elif cnt==1:
                result+=1
            elif cnt==2:
                result+=10
            elif cnt==3:
                result+=100
            else:
                result+=1000
    print(result)

if __name__=="__main__":
    main()