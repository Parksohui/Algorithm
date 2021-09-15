import math
if __name__=='__main__' :
    n=int(input())

    for i in range(n):
        x=int(input())

        for j in range(1,len(str(x))):
            if j==1:
                temp=10
            else:
                temp=10**j
            if int(str(x)[-j])>=5: #올림
                x=int(str(x)[:-j])*temp
                x+=temp
            else: # 내림
                x=int(str(x)[:-j])*temp

        print(x)
