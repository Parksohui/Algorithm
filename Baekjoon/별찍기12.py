if __name__=='__main__' :
    x=int(input())

    for i in reversed(range(x)):
        for j in range(i):
            print(" ", end='')
        for k in range(x-i):
            print("*",end='')
        print()

    for i in range(1,x):
        for j in range(i):
            print(" ", end='')
        for k in range(x-i):
            print("*", end='')
        print()



