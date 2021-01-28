if __name__ == '__main__' :
    x=int(input())

    for i in range(x):
        temp = input() #공백 입력
        count=int(input()) #학생 수
        sum=0

        for i in range(count): #사탕
            sum+=int(input())

        if(sum%count ==0):
            print("YES")
        else:
            print("NO")