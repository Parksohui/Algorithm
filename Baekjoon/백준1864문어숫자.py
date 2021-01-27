if __name__ == '__main__' :
    x=input()

    while(x!='#'):
        result = 0
        x=x[::-1]
        n=0
        temp=0
        for i in x:
            mul = 8 ** n #8진법
            if i=='-':
                temp=0
            elif i=="\\":
                temp=1
            elif i=="(":
                temp=2
            elif i=="@":
                temp=3
            elif i=="?":
                temp=4
            elif i==">":
                temp=5
            elif i=="&":
                temp=6
            elif i=="%":
                temp=7
            else:
                temp=-1
            result+=temp*mul
            n+=1
        print(result)
        x=input()
