if __name__ == '__main__' :
    x=input().split()
    y=int(input())

    for i in range(2):
        x[i]=int(x[i])

    x[1]=x[1]+y

    while(x[1]>=60): #분 
        x[1]=x[1]-60
        x[0]+=1
    while(x[0]>=24): #시
        x[0]=x[0]-24

    print(str(x[0])+" "+str(x[1]))