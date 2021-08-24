import sys

if __name__ == '__main__':

    x = int(sys.stdin.readline().strip())
    arr = [x]

    while x != 0:  # 입력_마지막 입력 0
        x = int(sys.stdin.readline().strip())
        if x != 0:
            arr.append(x)

    # 소수 판별
    prime = [True] * (max(arr) * 2)
    line = int(max(arr) * 2 * 0.5) + 1

    for i in range(2, line):
        if prime[i] == True:
            for j in range(i + i, max(arr) * 2, i):
                prime[j] = False

    for i in arr:  # n보다 크고 2n보다 작거나 같은 소수 개수 구하기
        cnt = 0
        if i == 1: # 1보다 크고 2보다 작거나 같은 소수 개수는 1개
            cnt = 1
        for j in range(i + 1, i * 2):
            if prime[j] == True:
                cnt += 1
        print(cnt)
