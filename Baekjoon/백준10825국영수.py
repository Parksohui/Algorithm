import sys
if __name__=='__main__' :
    N=int(sys.stdin.readline())

    arr=[]
    for i in range(N):
        arr.append(sys.stdin.readline().split())

    arr.sort(key=lambda x:(-int(x[1]), int(x[2]),-int(x[3]),x[0] ))

    for i in arr:
        print(i[0])