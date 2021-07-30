if __name__=='__main__' :
    N=int(input())

    arr=[]
    for i in range(N):
        arr.append(int(input()))

    cnt=0
    while(True):
        if max(arr)==arr[0] and arr.count(max(arr))==1: #종료 조건
            break
        else:
            arr[0]+=1 #기호 1번 한표 추가
            temp=arr[1::]
            arr[temp.index(max(temp))+1]-=1 #나머지에서 하나 빼기
            cnt+=1

    print(cnt)
