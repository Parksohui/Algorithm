if __name__=='__main__' :
    S=int(input())

    max=0
    min=0
    for i in range(S):
        if i*(i+1)/2>S:
            max=i
            break
        if i*(i+1)/2<=S:
            min=i

    print(min)
