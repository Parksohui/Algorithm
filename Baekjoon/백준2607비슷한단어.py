import sys

if __name__=='__main__' :
    T=int(sys.stdin.readline().strip())

    first=sys.stdin.readline().strip()
    dict={}
    for i in first: #dict key,value로 저장
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

    cnt=0
    for i in range(T-1):
        arr=dict.copy() #copy
        value=list(sys.stdin.readline().strip())

        for j in value:
            if j in dict: #dict에 있는 값이라면
                arr[j]-=1
            else:
                if j in arr: #dict에 있다면
                    arr[j]-=1
                else: #dict에 없는 값이라면
                    arr[j]=-1
        result=list(arr.values())
        check=list(map(abs,result))
        
        #합이 2보다 작고 -2보다 커야함
        #절댓값의 합이 2보다 작거나 같아야함
        if sum(result)<2 and sum(result)>-2 and sum(check)<=2:
            cnt+=1

    print(cnt)