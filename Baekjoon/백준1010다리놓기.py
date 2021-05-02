if __name__=='__main__':
    a=int(input())

    for i in range(a):
        x,y=map(int, input().split())

        temp=1
        if y!=0:
            for j in range(1,y+1):
                temp*=j

        temp2=1
        if y-x !=0:
            for j in range(1,y-x+1):
                temp2*=j

        temp3=1
        if x!=0:
            for j in range(1,x+1):
                temp3*=j

        result=temp/(temp2*temp3)  #조합 공식 사용
        print(int(result))