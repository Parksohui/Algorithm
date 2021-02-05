if __name__=='__main__' :
    x=int(input())

    temp=[]

    for i in range(x):
        temp.append(list(map(int,input().split())))
        
    #2번째 인자로 비교하기 위해 (y 값이 같으면 x 값을 비교하여 오름차순)
    temp.sort(key=lambda a:(a[1], a[0]))

    for i in range(x):
        print(temp[i][0],temp[i][1])