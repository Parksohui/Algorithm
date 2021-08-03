
if __name__=='__main__' :
    T=int(input())

    arr=[[1,0],[0,1]] #0,1일때
    N=[]
    for i in range(T):
        N.append(int(input()))

    for j in range(2,max(N)+1): #최대 구해야할 값 까지 구함
        arr.append([arr[j - 1][0] + arr[j - 2][0], arr[j - 1][1] + arr[j - 2][1]])

    for i in N: #출력
        print(arr[i][0], arr[i][1])



