if __name__=='__main__' :
    arr=list(input().split())

    result=[int(arr[0])] #수열 저장
    temp=[] #제거되는 것 저장
    x=arr[0] # 수

    while True:
        sum=0 #합
        for i in str(x):
            sum+=int(i)**int(arr[1]) #수열 구하기
            x=sum

        if sum in result: #반복되는 것이라면 제거
            temp.append(sum) #제거된 것인걸 저장하기 위해 
            result.remove(sum) #제거
        elif sum in temp: #이미 제거되었던 것이라면 계속 반복 break
            break
        else: #처음 나오는 수라면
            result.append(sum)

    print(len(result))