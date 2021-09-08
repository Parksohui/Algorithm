import sys

if __name__=='__main__' :
    N=int(sys.stdin.readline().strip())

    arr=[]
    for i in range(N): # 입력
        arr.append(int(sys.stdin.readline().strip()))

    arr.sort(reverse=True) # 내림차순 정렬

    result=0
    for i in range(N): # 나머지가 2가 아닌 것만 추가
        if i%3 != 2:
            result+=arr[i]

    print(result)