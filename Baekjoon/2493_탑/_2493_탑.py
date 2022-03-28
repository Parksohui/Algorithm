import sys

if __name__=='__main__':
    n=int(input()) # 탑의 수

    arr=list(map(int, sys.stdin.readline().split())) # 탑의 높이

    stack=[]
    answer=[]

    for i in range(len(arr)):
        while True:
            if len(stack)==0: # 레이저 신호 수신하는 탑 존재 x
                answer.append(str(0))
                stack.append([str(i+1), arr[i]])
                break
            elif stack[-1][1]<arr[i]: # 왼쪽 탑의 높이가 더 낮으면
                stack.pop()
            else: # 왼쪽 탑의 높이가 높거나 같으면
                answer.append(stack[-1][0])
                stack.append([str(i+1), arr[i]])
                break

    print(' '.join(answer))
