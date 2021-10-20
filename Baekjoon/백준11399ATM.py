import sys

if __name__=='__main__':
    N=int(input()) # 사람의 수
    arr=list(map(int, sys.stdin.readline().split())) # 사람이 돈을 인출하는데 걸리는 시간

    arr.sort() # 정렬
    dp=[arr[0]] 
    for i in range(1,len(arr)): # dp
        dp.append(dp[-1]+arr[i])

    print(sum(dp)) # 총 합