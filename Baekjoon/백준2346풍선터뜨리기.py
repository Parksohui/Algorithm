import sys

if __name__=='__main__':
    n=int(sys.stdin.readline().strip())

    arr=list(map(int,sys.stdin.readline().split()))
    for i in range(n): # [이동할 값, index]
        arr[i]=[arr[i],i+1]

    answer=[]
    idx=0
    while len(arr)!=0:
        x=arr.pop(idx) # 풍선 터뜨림
        answer.append(x[1]) # answer에 index 추가
        if len(arr)==0: # 종료 조건
            break
        if x[0]<0: # 이동할 값이 음수면
            idx=(idx+x[0])%len(arr)
        else: # 이동할 값이 양수면
            idx=(idx+x[0]-1)%len(arr)

    print(' '.join(map(str,answer)))

