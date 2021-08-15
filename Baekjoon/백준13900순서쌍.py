import  sys

# 조합, sum, 이중 for문, while 쓰는 경우 시간 초과 발생
# ex) 2 3 4 이면 (2+3)*4 + 2 * 3 이런식으로 접근
# 위의 방법으로 접글할때도 sum() 사용하면 시간 초과 발생

if __name__=='__main__' :
    N=sys.stdin.readline().strip()

    arr=list(map(int,sys.stdin.readline().split()))

    sum=[arr[0]]
    for i in range(1,len(arr)):
        sum.append(sum[-1]+arr[i])

    result = 0
    for i in range(1,len(arr)):
        result+=sum[i-1]*arr[i]

    print(result)
