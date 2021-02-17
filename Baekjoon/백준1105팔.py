if __name__=='__main__' :
    L,R=input().split() #L,R 입력

    minvalue=0 #길이 다르면 8이 0개

    if len(L)==len(R): #길이 같으면
        for i in range(len(L)):
            if L[i]==R[i]: #값이 같으면
                if L[i]=='8': #8이면
                    minvalue+=1
            else: #값이 다르면
                break

    print(minvalue)
