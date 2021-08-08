if __name__=='__main__' :
    N=int(input())

    #문제) 자신보다 낮은 값이 몇개 있는가
    x=input().split()
    arr=list(map(int,x))
    temp=sorted(set(map(int,x))) #set 후에 정렬 -> 낮은 값 부터 나옴

    #dict 시간복잡도 O(1) 
    dict={temp[i]:i for i in range(len(temp))}

    for i in arr:
        print(dict[i],end=" ")
