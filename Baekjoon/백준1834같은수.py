if __name__=='__main__' :
    N=int(input()) 

    result=0
    for i in range(1,N):
        result+= N*i+i #나머지와 몫이 같은 자연수 구하기

    print(result)