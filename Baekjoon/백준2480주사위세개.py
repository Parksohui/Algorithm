if __name__ == '__main__' :
    x=input().split()

    for i in range(3): #숫자로 change
        x[i]=int(x[i])

    maxcount=0
    maxvalue=0
    answer=0

    for i in range(3):
        if(maxcount<x.count(x[i])): #같은 눈 개수
            maxcount=x.count(x[i])
            maxvalue=x[i]

    if(maxcount==3): #같은 눈 3
        answer=10000+x[0]*1000
    elif(maxcount==2): #같은 눈 2
        answer=1000+maxvalue*100
    else: #모두 다른 눈
        answer=max(x)*100

    print(answer)


