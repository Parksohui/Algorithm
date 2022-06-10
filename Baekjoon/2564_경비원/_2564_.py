import sys

def main():
    m,n=map(int,sys.stdin.readline().split())

    k=int(input())
    arr=[]

    for i in range(k+1):
        a,d=map(int,sys.stdin.readline().split())
        if a==1: # 북
            arr.append([0,d])
        elif a==2: # 남
            arr.append([n, d])
        elif a==3: # 서
            arr.append([d, 0])
        else: # 동
            arr.append([d, m])

    answer=0
    val=arr[-1]
    for i in range(k):
        if arr[i][0]!=val[0] :
            temp = val[0] - arr[i][0]
            if temp < 0:
                temp = -temp
            if arr[i][1]+val[1]<m-arr[i][1]+m-val[1]:
                temp+=(arr[i][1]+val[1])
            else:
                temp+=m-arr[i][1]+m-val[1]
        else:
            if arr[i][1]-val[1]==m or val[1]-arr[i][1]==m: # 동, 서
                temp = m
                if arr[i][0] + val[0] < n - arr[i][0] + n - val[0]:
                    temp += (arr[i][0] + val[0])
                else:
                    temp += n - arr[i][0] + n - val[0]
            else: # 같은 줄
                temp=arr[i][1]-val[1]
                if temp<0:
                    temp=-temp
        answer+=temp
    print(answer)

if __name__=='__main__':
    main()