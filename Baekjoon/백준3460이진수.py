if __name__ == '__main__' :
    x=int(input())

    for i in range(x):
        y=int(input())
        temp=format(y,'b') #10진수 -> 2진수

        temp=temp[::-1]
        for i in range(len(temp)):
            if temp[i]=='1':
                print(i,end=' ')