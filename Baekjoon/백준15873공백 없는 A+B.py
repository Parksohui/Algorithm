if __name__ == '__main__' :
    x=input()

    if(x[1]=="0"): #A가 10인 경우
        A=10
    else: #A가 한자리 수 
        A=int(x[0])

    if(len(x)==2): #길이가 2이면 -> A,B 한자리 수
        B=int(x[1])
    elif(len(x)==3): #길이가 3이면 
        if(x[2]=="0"): #B가 10인 경우
            B=int(x[1::])
        else: #B가 한자리 수
            B=int(x[2])
    else: #B가 10인 경우
        B=10

    print(A+B)
