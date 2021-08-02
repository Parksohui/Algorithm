if __name__=='__main__' :
    N=int(input())
    M=int(input())
    S=input()

    temp='' #Pn
    if N!=1:
        for i in range(N):
          temp+='IO'
        temp+='I'
    else:
        temp='IOI'

    result=0
    for i in range(M-len(temp)):
        check=0
        for j in range(len(temp)):
            if S[i+j]==temp[j]:
                check+=1
                if check==len(temp):
                    result+=1
            else:
                continue

    print(result)
