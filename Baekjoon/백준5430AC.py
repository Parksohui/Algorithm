from collections import deque
import sys

if __name__=='__main__' :
    x=int(sys.stdin.readline()) #테스트 케이스 개수

    for i in range(x):
        y=input() #수행할 함수

        cnt=int(sys.stdin.readline()) #배열 수

        temp=sys.stdin.readline() #배열 

        if cnt == 0: #빈 배열
            if y.count("D")>0: #D 함수가 있으면
                print("error")
            else: #없으면
                print("[]")
            continue
        else: #빈 배열이 아니면
            temp=temp[1:-2] #괄호 제거
            if len(temp)==1: #숫자 하나면
                k=deque([int(temp[0])])
            else: #값이 여러개면
                k=deque(map(int,temp.split(",")))

        result=True #배열 길이
        Rnum=0 #R 개수 count
        for j in y:
            if j=="R":
                Rnum+=1
            elif j=="D":
                if len(k)==0: #길이가 0이면 error
                    result=False
                else:
                    if Rnum%2==0: #R이 짝수이면 원래대로
                        k.popleft()
                    else: #R이 홀수이면 뒤에서 제거
                        k.pop()

        if result==True: #error가 아니면
            if Rnum%2!=0: #홀수이면 뒤집어주기
                k.reverse()
            print("[",end='')
            for i in range(len(k)):
                if i!=len(k)-1:
                    print(k[i],end=',')
                else:
                    print(k[i],end='')
            print("]")
        else: #error이면
            print("error")