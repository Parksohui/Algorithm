import sys

if __name__=='__main__' :
    x=int(sys.stdin.readline().strip())
    
    #카드 유무 판별_set 사용
    card=set(map(int,sys.stdin.readline().split()))

    y=int(sys.stdin.readline().strip())

    find=list(map(int,sys.stdin.readline().split()))

    for i in find:
        if i in card:
            print(1, end=" ")
        else:
            print(0, end=" ")