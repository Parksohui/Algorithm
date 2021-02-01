if __name__=='__main__' :
    x=list(map(int,input().split()))

    while(True):
        if sum(x)==0: #종료조건: 0 0 0 입력
            break
            
        x.sort()

        if x[2]**2 == x[0]**2 + x[1]**2: #직각 삼각형 조건
            print("right")
        else:
            print("wrong")

        x = list(map(int, input().split()))