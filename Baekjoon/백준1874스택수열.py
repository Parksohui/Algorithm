import sys

if __name__=='__main__':
    n=int(sys.stdin.readline().strip())

    arr=[]
    for i in range(n): #수열 입력
        arr.append(int(sys.stdin.readline().strip()))

    idx=0
    idx_stack=1
    temp=[] #오름차순 push
    answer=[] # +,-
    result=[] # 만들어진 수열
    while True:
        if idx>=n or idx_stack>n+1: #종료 조건
            break
        if len(temp)!=0 and temp[-1]==arr[idx]: #temp에 이미 있는 값 pop
            result.append(temp.pop())
            answer.append("-")
            idx+=1
        elif arr[idx]!=idx_stack: # push
            temp.append(idx_stack)
            idx_stack+=1
            answer.append("+")
        elif arr[idx]==idx_stack: # 넣으려는 값이 필요한 값이면
            result.append(idx_stack) # push 전에 바로 result에 추가
            answer.append("+") # puxh
            answer.append("-") # pop
            idx_stack+=1
            idx+=1

    if arr==result: # 만들어진 수열이 입력 수열과 같으면
        for i in answer:
            print(i)
    else: # 불가능한 경우
        print("NO")