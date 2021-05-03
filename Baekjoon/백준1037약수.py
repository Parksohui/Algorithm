if __name__ =='__main__':
    a=int(input())

    arr=list(map(int, input().split()))

    arr.sort() #정렬

    answer=arr[0]*arr[-1] #처음과 끝 곱함 

    print(answer)