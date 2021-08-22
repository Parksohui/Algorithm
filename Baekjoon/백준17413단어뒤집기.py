import sys

if __name__=='__main__' :
    S=sys.stdin.readline().strip()

    arr=[]
    result=""
    check=False
    for i in S:
        if i=="<": #태그 시작
            if len(arr)!=0: #앞에 단어가 있었다면
                arr.reverse() #뒤집기
                result+=''.join(arr)
                arr=[]
            check=True
            result+="<"
        elif i==">": #태그 끝
            check=False
            result+=">"
        elif check==True: #태그라면
            result+=i
        else: #단어
            if i==" ": #공백
                if len(arr)!=0: #뒤집기
                    arr.reverse()
                    result+=''.join(arr)
                    arr=[]
                result+=i
            else:
                arr.append(i)

    if len(arr)!=0: #끝
        arr.reverse()
        result+=''.join(arr)

    print(result)