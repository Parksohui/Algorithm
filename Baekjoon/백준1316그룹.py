if __name__=='__main__' :
    x=int(input())
    result=0

    for i in range(x):
        temp=input()
        value=[]

        bol=True
        value.append(temp[0])
        for j in range(1,len(temp)):
            if temp[j]==temp[j-1]: #연속한다면
                pass
            else: #연속하지 않으면
                if temp[j] in value: #이미 나왔던 문자라면
                    bol=False
                    break
                else: #처음 나오는 문자라면
                    value.append(temp[j])

        if bol==True:
            result+=1
    print(result)


