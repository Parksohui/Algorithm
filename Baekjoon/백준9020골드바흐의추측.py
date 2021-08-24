import sys

if __name__ == '__main__':

    x = int(sys.stdin.readline().strip())

    arr = []
    for i in range(x): #입력
        y=int(sys.stdin.readline().strip())
        arr.append(y)

    # 소수 판별
    prime = [True] * max(arr)
    primenum=[] #소수 값만 따로 저장
    for i in range(2, max(arr)):
        if prime[i] == True:
            primenum.append(i)
            for j in range(i + i, max(arr), i):
                prime[j] = False

    for i in arr:
        temp=[0,0,10000] #값, 값, 차이
        for j in range(len(primenum)): #소수 값
            if prime[i-primenum[j]]==True: # 구하는 값 - 소수= 소수 이면
                if abs(i-2*primenum[j])<temp[2]: # 두 소수의 차이가 작으면
                    temp=[primenum[j],i-primenum[j],abs(i-2*primenum[j])]
        print(temp[0],temp[1])
