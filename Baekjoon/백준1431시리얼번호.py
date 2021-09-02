import sys

if __name__=='__main__':
    N=int(sys.stdin.readline().strip())

    arr=[]
    for i in range(N):
        x=sys.stdin.readline().strip()

        temp=0
        for j in x: #자리수의 합 구하기 (숫자인 것만)
            if j.isdigit():
                temp+=int(j)

        arr.append([x,temp])
    
    # 조건) 1. 길이 비교 2. 자리수 합 비교 3. 사전순 비교
    arr.sort(key=lambda x:(len(x[0]),x[1],x[0]))

    for i in range(N):
        print(arr[i][0])
