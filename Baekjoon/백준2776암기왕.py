import sys
if __name__=='__main__' :
    T=int(sys.stdin.readline().strip())

    for i in range(T):
        N=int(sys.stdin.readline().strip())
        arr=set(map(int,sys.stdin.readline().split())) #set

        M=int(sys.stdin.readline().strip())
        arr2=list(map(int,sys.stdin.readline().split()))

        for i in arr2:
            if i in arr: #수첩 1에 있으면
                print(1)
            else: #수첩 1에 없으면
                print(0)

