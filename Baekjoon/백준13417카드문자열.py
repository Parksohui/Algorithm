import sys

if __name__=='__main__':
    T=int(input()) # 테스트 케이스 개수

    for i in range(T):
        N=int(input()) # 카드의 개수
        arr=list(sys.stdin.readline().strip().split()) # 카드 입력

        answer=arr[0] # 처음 카드는 자신의 앞에 놓음
        for i in range(1, len(arr)):
            if ord(answer[0])>=ord(arr[i]): # 사전 순으로 앞이면
                answer=arr[i]+answer
            else: # 사전 순으로 뒤면
                answer+=arr[i]
        print(answer)
