import sys

if __name__=='__main__' :
    N=int(sys.stdin.readline().strip())

    arr=[0]*N
    for i in range(N): #입력
        arr[i]=float(sys.stdin.readline().strip())

    dp=[arr[0]]
    for i in range(1,N): #전 값과 곱했을때와 현재 배열 값 중 큰 값으로 저장
        dp.append(max(arr[i], dp[-1]*arr[i]))

    print("{:.3f}".format(max(dp),3)) #최댓값을 소수점 이하 셋째 자리까지 출력