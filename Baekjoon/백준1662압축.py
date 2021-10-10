import sys

if __name__=='__main__':
    line=sys.stdin.readline().strip()

    result=0 # 길이
    stack=[]
    Qlen=0
    for i in line:
        if i==')': # K(Q) 계산
            temp=0
            while True: # '(' 만날때 까지 반복
                if stack[-1]=='(': # 종료 조건
                    stack.pop()
                    break
                x = stack.pop() # Q 구하기
                if x[-1]=='-':
                    temp+=int(x[:-1]) # 압축 풀어진 길이
                else: # 길이
                    Qlen+=1
            K=stack.pop() # K
            # 문자열이 아닌 압축 푼 길이라는 것을 '-'추가하여 표시
            result=str(int(K)*(Qlen+temp))+'-'
            stack.append(result)
            Qlen=0
        else: # 추가
            stack.append(i)

    answer=0
    for i in stack:
        if i[-1]=='-': # 압축 풀어진 길이
            answer+=int(i[:-1])
        else: # 문자열
            answer+=1
    print(answer)