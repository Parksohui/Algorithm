if __name__ == '__main__' :
    x=input().split()
    y=int(input())

    for i in range(3):
        x[i]=int(x[i])

    x[2]=x[2]+y

    while(x[2]>=60): #초
        x[2]-=60
        x[1]+=1
    while(x[1]>=60): #분
        x[1]-=60
        x[0]+=1
    while(x[0]>=24): #시
        x[0]-=24

    print(str(x[0])+" "+str(x[1])+" "+str(x[2]))