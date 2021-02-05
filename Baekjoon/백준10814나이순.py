if __name__=='__main__' :
    x=int(input())

    result=[]
    for i in range(x):
        result.append(input().split())
        result[i].append(i) #가입한 순서를 위해 index 추가
        result[i][0]=int(result[i][0]) #나이는 str -> int

    result.sort(key=lambda x:(x[0], x[2])) #나이순으로 정렬 후 나이가 같으면 가입 순으로 정렬

    for i in range(x):
        print(result[i][0],result[i][1])