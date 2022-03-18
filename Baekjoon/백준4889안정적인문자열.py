import sys

if __name__=='__main__':
    num=1

    while True:
        data=sys.stdin.readline().strip()
        if data.count('-')>0: # 종료 조건
            break

        stack_left=[] # {
        stack_right=[] # }
        cnt=0
        for i in data:
            if i=='{':
                stack_left.append(i)
            else:
                if len(stack_left)==0:
                    stack_right.append(i)
                else: # 안정적
                    stack_left.pop()

        # 안정적으로 바꾸는데 필요한 최소 연산의 수
        if len(stack_left)!=0:
            cnt+=len(stack_left)//2+len(stack_left)%2
        if len(stack_right)!=0:
            cnt+=len(stack_right)//2+len(stack_right)%2

        print(str(num)+'. '+str(cnt))
        num+=1