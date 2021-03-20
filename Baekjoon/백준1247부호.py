import sys

if __name__=='__main__' :

    for i in range(3):
        x = int(sys.stdin.readline().strip())

        sum=0

        for j in range(x):
            sum+=int(sys.stdin.readline().strip())


        if sum==0:
            print("0")
        elif sum>0:
            print("+")
        else:
            print("-")