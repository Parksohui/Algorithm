
if __name__=='__main__':
    arr=[True]*2000000
    line=int((2000000)*0.5)
    arr[1]=False

    n=int(input())

    for i in range(2, line+1): # 소수 판별
        if arr[i]==True:
            for j in range(i+i, 2000000, i):
                arr[j]=False

    flag=False
    for i in range(n, 2000000):
        cnt = 0
        if arr[i]==True: # 소수이면
            i = str(i)
            for j in range(len(i)//2): # 팰린드롬
                if i[j]==i[len(i)-1-j]:
                    cnt+=1
                else:
                    break
            if cnt==len(str(i))//2:
                print(i)
                flag=True
                break
        if flag==True:
            break