if __name__=='__main__':

    a=int(input())
    while(a !=0):

        arr=[input() for i in range(a)] #입력

        arrtemp=[i.upper() for i in arr] #대문자로 바꿔줌

        arrtemp.sort() #정렬

        for i in arr: #사전순으로 가장 앞서는 단어 출력
            temp=i.upper()
            if temp==arrtemp[0]: 
                print(i)
                break
        a=int(input())


