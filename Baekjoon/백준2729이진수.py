import sys

if __name__=='__main__' :

    T=int(sys.stdin.readline().strip())

    for i in range(T):
        num=sys.stdin.readline().split()

        num1=int(num[0],2) #2진수->10진수
        num2=int(num[1],2)

        print(format(num1+num2,'b')) #10진수->2진수

