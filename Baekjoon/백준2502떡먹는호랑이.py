import sys

if __name__=='__main__':
    D,K=map(int, sys.stdin.readline().split()) # 넘어온 날, 떡의 개수

    arr=[[1,0],[0,1]] 

    for i in range(2,D):
        arr.append([arr[i-1][0]+arr[i-2][0], arr[i-1][1]+arr[i-2][1]])

    a_temp=arr[-1][0]
    b_temp=arr[-1][1]
    a=1
    b=-1

    while True: # 첫 날, 둘째 날 떡의 개수 구하기
        temp=K-(a_temp*a)
        if temp%b_temp==0:
            b=temp//b_temp
            break
        else:
            a+=1

    print(a) # 첫 날
    print(b) # 둘째 날
