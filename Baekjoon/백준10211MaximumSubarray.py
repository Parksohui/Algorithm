import sys

if __name__=='__main__':
    T=int(input()) # 테스트 케이스 수

    for i in range(T):
        N=int(input()) # 크기
        arr=list(map(int, sys.stdin.readline().split())) # X의 내용

        maxsum=min(arr) # 최솟값을 maximum으로 설정
        for j in range(len(arr)):
            sum = 0
            for k in range(j,len(arr)):
                sum+=arr[k]
                if sum>maxsum: # maximum subarray 찾기
                    maxsum=sum
        print(maxsum)
