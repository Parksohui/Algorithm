if __name__ == '__main__' :
    A=list(input())
    B=list(input())

    i=0
    while(i<len(A)):
        if B.count(A[i])>0:
            B.remove(A[i])
            A.remove(A[i])
        else:
            i+=1

    print(len(A)+len(B))
