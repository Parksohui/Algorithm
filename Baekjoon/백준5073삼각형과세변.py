if __name__=='__main__' :
    x=list(map(int,input().split()))

    while(sum(x)!=0):
        x.sort()
        if x[0]+x[1]<=x[2]: #삼각형 조건 x
            print("Invalid")
        elif x.count(x[0])==3: #세 변 길이 같음
            print("Equilateral")
        elif x[0]==x[1] or x[1]==x[2]: #두 변의 길이만 같음
            print("Isosceles")
        else: #세 변의 길이가 모두 다른 경우
            print("Scalene")
        x = list(map(int, input().split()))




