if __name__=='__main__' :
    x=int(input())

    temp=[]

    for i in range(x):
        temp.append(list(map(int,input().split())))

    temp.sort()

    for i in range(x):
        print(temp[i][0],temp[i][1])