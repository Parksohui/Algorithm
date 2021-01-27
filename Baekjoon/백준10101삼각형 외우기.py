if __name__ == '__main__' :
    x=[]

    for i in range(3):
        x.append(int(input()))

    x.sort()

    if(sum(x)==180):
        if x.count(60)==3: #세 각의 크기가 모두 60이면
            print("Equilateral")

        elif x[0]==x[1] or x[1]==x[2]: #두 각이 같은 경우
            print("Isosceles")

        elif x.count(x[0])==1 and x.count(x[1])==1: #같은 각이 없는 경우
            print("Scalene")

    else: #세 각의 합이 180이 아닌 경우
        print("Error")
