if __name__=='__main__' :
    T=int(input())

    for i in range(T):
        k=int(input())

        num=0
        for j in range(k):
            num+=0.5
            num*=2
            
        print(int(num))