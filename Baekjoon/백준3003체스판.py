if __name__ == '__main__' :

    temp=[1,1,2,2,2,8] #체스 피스 개수
    x = input().split() #입력

    for i in range(6):
        print(temp[i]-int(x[i]),end=' ')