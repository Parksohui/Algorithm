if __name__=='__main__' :
    x=input()

    while(x!='.'):
        answer=1
        result=[]
        for i in range(len(x)):
            if(x[i]=='[' or x[i]=='('): #추가
                result.append(x[i])

            if(x[i]==')'):
                if len(result)!=0:
                    if result[-1]=='(': #짝이 맞으면
                        result.pop()
                    else:
                        answer=0
                else:
                    answer=0
                    break
            elif(x[i]==']'):
                if len(result) != 0:
                    if result[-1]=='[': #짝이 맞으면
                        result.pop()
                    else:
                        answer=0
                else:
                    answer=0
                    break

        if len(result)!=0: #길이가 0이 아니면 균형 x
            answer=0

        if answer==0:
            print("no")
        else:
            print("yes")

        x = input()

