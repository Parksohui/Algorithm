import sys

if __name__=='__main__':
    T=int(input()) # 테스트 케이스 수
    for i in range(T):
        input()
        N,M=map(int, sys.stdin.readline().split()) # 각 병사 수
        S=list(map(int, sys.stdin.readline().split())) # 세준
        B=list(map(int, sys.stdin.readline().split())) # 세비
        
        # 최댓값을 가진 쪽이 승리하므로 최댓값 구하기
        maxS = max(S) 
        maxB = max(B)

        if maxS<maxB: # 세비의 최댓값이 더 클때
            print("B")
        elif maxS>=maxB: # 세준이의 최댓값이 더 크거나 같을때
            print("S")
        else: # 그 외
            print("C")