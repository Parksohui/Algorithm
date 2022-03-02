import sys

if __name__=='__main__':
    t=int(input()) # 테스트 케이스 개수

    for i in range(t):
        n=int(input()) # 전화번호 수
        arr=[]
        for j in range(n):
            str=sys.stdin.readline().replace(' ','').strip() # 입력
            arr.append(str)
        arr.sort() # 정렬
        bool=False # 일관성 check
        for j in range(n-1):
            if arr[j]==arr[j+1][:len(arr[j])]:
                bool=True
        if bool==True:
            print("NO")
        else:
            print("YES")