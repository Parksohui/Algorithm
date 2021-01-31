if __name__ == '__main__' :
    x=int(input())

    result=x//5 #1분에 5까지 갈 수 있으므로 멀리 갈 수 있는 시간

    if(x%5 !=0): # 나머지가 있으면 1분 추가
        result+=1

    print(result)