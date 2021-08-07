if __name__=='__main__' :
    N=int(input())

    result=0
    for i in range(1,N+1):
        i=str(i)
        if len(i)==1 or len(i)==2: #한자리, 두자리 수는 한수
            result+=1
        else:
            temp=int(i[1]) -int(i[0]) #수 차이 
            cnt=0
            for j in range(1,len(i)-1): #연속된 두 수 차이 비교
                if temp==int(i[j+1])-int(i[j]):
                    cnt+=1
                    if cnt==len(i)-2: # 한수
                        result+=1
                else:
                    break

    print(result)




