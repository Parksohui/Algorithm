if __name__=='__main__':

    a=int(input())

    arr=dict()

    for i in range(a):
        temp=input().split()

        arr[temp[0]]=temp[1] #딕셔너리 추가

    answer=[]
    for key,value in arr.items(): #value가 enter인 key값 찾기
        if value=='enter':
            answer.append(key)

    answer.sort(reverse=True) #역순으로 정렬

    for i in answer:
        print(i)