if __name__=='__main__' :

    x = input().split()

    while(True):
        if x[0]=='0' and x[1]=='0': #종료조건
            break
        carry=0
        a=list(map(int,(x[0][::-1])))
        b=list(map(int,(x[1][::-1])))

        #min,max value 구하기
        minvalue=0
        maxvalue=0
        maxtemp=[]

        if(len(a)>=len(b)):
            minvalue=len(b)
            maxvalue=len(a)
            maxtemp=a
        else:
            minvalue=len(a)
            maxvalue=len(b)
            maxtemp=b

        temp=[0 for i in range(maxvalue+1)] #carry 값

        for i in range(minvalue): #두 수, carry 더하기
            if a[i]+b[i]+temp[i] >9:
                temp[i+1]+=1
                carry+=1
        for i in range(minvalue, maxvalue): #carry와 나머지 한 수 더하기
            if maxtemp[i]+temp[i] > 9:
                temp[i+1]+=1
                carry+=1

        print(carry)
        x=input().split()
