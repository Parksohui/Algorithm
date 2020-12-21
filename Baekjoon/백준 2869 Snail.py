if __name__ == '__main__':
    A,B,V=input().split()

    A=int(A)
    B=int(B)
    V=int(V)

    if (V-B)%(A-B)!=0:
       day=(V-B)/(A-B) + 1
    else:
        day=(V-B)/(A-B)

    print(int(day))