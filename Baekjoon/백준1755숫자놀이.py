if __name__=='__main__':
    a,b=input().split()

    arr=[]
    for i in range(int(a),int(b)+1):
        text=''
        for j in str(i): #string 으로 읽기
            j=int(j)
            if j==0:
              text+='zero '
            elif j==1:
                text+='one '
            elif j==2:
                text+='two '
            elif j==3:
                text+='three '
            elif j==4:
                text+='four '
            elif j==5:
                text+='five '
            elif j==6:
                text+='six '
            elif j==7:
                text+='seven '
            elif j==8:
                text+='eight '
            elif j==9:
                text+='nine '
        arr.append([i,text])
    arr.sort(key=lambda x: x[1]) #이차원 배열 -> 2번째 값으로 정렬

    num=0
    for i in arr: #출력
        num+=1
        print(i[0], end=' ')

        if num==10: #10개씩 출력
            num=0
            print()