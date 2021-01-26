if __name__ == '__main__' :
    x=int(input())

    temp=[]

    a=list(input())
    for i in range(x-1):
        temp.append(input())

    while(len(temp)!=0): #list 빌때까지 반복
        b=temp.pop()
        for i in range(len(a)):
            if(a[i]!=b[i]): #다르면 ?로 교체
                a[i]='?'
    print(''.join(a))

