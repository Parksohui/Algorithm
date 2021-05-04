if __name__=='__main__':
    a=int(input())

    line=64 #처음 가지고 있는 막대기

    answer=0 #막대기 수
    result=0 #막대기 길이

    while result!=a:
        if a==64: #64만드려면 끝
            answer=1
            break

        line=line/2 #절반으로 자름

        if result+line <= a: #원하는 값보다 작거나 같으면 막대기 붙이기
            result+=line
            answer += 1

    print(answer)




