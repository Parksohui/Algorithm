import sys
input=sys.stdin.readline

if __name__=='__main__' :
    S=input().strip() #입력

    stack=[]
    cnt=0

    for i in S:
        if len(stack)==0: #stack이 비어있으면
            if i==")": # ) 이면 ( 필요
                cnt+=1
            else: # ( 추가
                stack.append(i)
        else:
            if i==")": # ( 짝 제거
                stack.pop()
            else: # ( 추가
                stack.append(i)

    cnt+=len(stack) # stack 길이 = 필요한 괄호

    print(cnt)
