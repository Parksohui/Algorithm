import sys #입력 시간 단축을 위해 sys사용

if __name__=='__main__' :
    temp=sys.stdin.readline().strip() #입력

    result=True

    stack=[]

    for i in range(len(temp)):
        if temp[i]=='(':
            stack.append(temp[i])
        elif temp[i]=='[':
            stack.append(temp[i])
        elif temp[i]==')':
            if(len(stack)==0): #잘못된 괄호 이므로 False
                result=False
                break
            x=True
            y=[]
            while x:
                if len(stack)!=0 and type(stack[-1])==int: #숫자 뽑아냄
                    y.append(stack.pop())
                else:
                    x=False
            if len(stack)!=0:
                k=stack.pop()
                if k=='(': #올바른 괄호
                    if len(y)==0:
                        stack.append(2)
                    else:
                        stack.append(2*(sum(y)))
                else: #올바르지 않은 괄호
                    result=False
                    break
            else: #올바르지 않은 괄호
                result=False
                break

        elif temp[i]==']':
            if (len(stack) == 0): #잘못된 괄호 이므로 False
                result = False
                break
            x = True
            y = []
            while x:
                if len(stack)!=0 and type(stack[-1])==int: #숫자 뽑아냄
                    y.append(stack.pop())
                else:
                    x = False
            if len(stack) != 0:
                k = stack.pop()
                if k == '[': #올바른 괄호
                    if len(y) == 0:
                        stack.append(3)
                    else:
                        stack.append(3 * (sum(y)))
                else: #올바르지 않은 괄호
                    result = False
                    break
            else: #올바르지 않은 괄호
                result=False
                break
        else: #올바르지 않은 괄호
            result=False
            break

    for i in range(len(stack)): #int가 아닌 값이 있으면 올바르지 않은 괄호
        if type(stack[i])!=int:
            result=False
            break

    if result==False: #올바르지 못한 괄호열이면 0 출력
        print(0)
    else: #올바른 괄호열이면 합 출력
        print(sum(stack))

