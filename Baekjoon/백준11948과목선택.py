if __name__ == '__main__' :
    Science=[]
    Social=[]

    for i in range(4):
        Science.append(int(input()))
    for i in range(2):
        Social.append(int(input()))

    Science.sort()

    result=0
    result+=sum(Science[1::]) #4과목 중 큰 과목 3과목 선택
    result+=max(Social) #2과목 중 큰 한 과목

    print(result)
