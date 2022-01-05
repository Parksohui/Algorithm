import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().strip())

    for i in range(t):
        x=sys.stdin.readline().strip()

        left=[]
        right=[]
        for j in x:
            if j=='<': # 커서 왼쪽으로 이동
                if len(left)!=0:
                    right.append(left.pop())
            elif j=='>': # 커서 오르쪽으로 이동
                if len(right)>0:
                    left.append(right.pop())
            elif j=='-': # 백스페이스
                if len(left)!=0:
                    left.pop()
            else: # 글자 입력
                left.append(j)

        arr=left+list(reversed(right)) # right를 뒤집어서 left와 붙이기

        print(''.join(arr))