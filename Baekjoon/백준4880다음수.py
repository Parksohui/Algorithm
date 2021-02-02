if __name__=='__main__' :
    x=list(map(int,input().split()))

    while(True):
        if x[0]==0 and x[1]==0 and x[2]==0: #종료 조건
            break
        if x[1]-x[0]!=0 and x[1]-x[0]==x[2]-x[1]: #등차
            print("AP",x[2]+x[1]-x[0])
        else: #등비
            print("GP", int(x[2]*(x[1]/x[0])))

        x = list(map(int, input().split()))