import sys
if __name__=='__main__':
    a=int(input())

    answer=set() #set
    for i in range(a):
        b=sys.stdin.readline().split()

        if b[0]=='add': #추가(이미 있다면 무시) -> set은 중복 혀용 x
            answer.add(int(b[1]))
        elif b[0]=='remove': #제거(없는 경우 무시)
            if int(b[1]) in answer:
                answer.remove(int(b[1]))
        elif b[0]=='check': #있으면 1, 없으면 0 출력
            if int(b[1]) in answer:
                print(1)
            else:
                print(0)
        elif b[0]=='toggle': #있으면 제거, 없으면 추가
            if int(b[1]) in answer:
                answer.remove(int(b[1]))
            else:
                answer.add(int(b[1]))
        elif b[0]=='all': #바꿈
            answer={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        elif b[0]=='empty': #공집합
            answer.clear()
