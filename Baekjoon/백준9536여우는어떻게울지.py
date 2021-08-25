import sys
input=sys.stdin.readline

if __name__=='__main__' :
    T=int(input().strip())

    for i in range(T):
        say=list(input().split()) #녹음된 소리 입력

        arr=[]
        while True:
            x=input().strip()
            if x=="what does the fox say?": #마지막 줄
                break
            else:
                x=list(x.split())
                arr.append(x[-1]) #울음소리 저장

        result=[]
        for j in say:
            if j not in arr: #fox 울음소리가 아니라면
                result.append(j)

        print(' '.join(result))