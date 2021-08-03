import sys
if __name__=='__main__' :
    str=sys.stdin.readline().strip()
    bomb=sys.stdin.readline().strip()

    stack=[]
    for i in str:
        stack.append(i)
        if stack[-1]==bomb[-1]:
            if ''.join(stack[-len(bomb):])==bomb:
                    del stack[-len(bomb):]

    if len(stack)!=0:
        print(''.join(stack))
    else:
        print("FRULA")

