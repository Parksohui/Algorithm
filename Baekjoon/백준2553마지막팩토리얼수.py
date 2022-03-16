
if __name__=='__main__':
    n=int(input())

    result=1
    for i in range(2,n+1): # N! 계산
        result*=i

    result=str(result)[::-1] # 뒤집기
    for i in result: # 0이 아닌 가장 낮은 자리 수 출력
        if i!='0':
            print(i)
            break