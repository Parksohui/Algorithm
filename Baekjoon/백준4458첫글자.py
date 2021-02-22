import sys

if __name__=='__main__' :
    x=int(input())

    for i in range(x):
        st=list(sys.stdin.readline().strip()) #마지막 개행문자 제외하고 list로 변환

        st[0]=st[0].upper() #첫글자를 대문자로 바꿈

        print(''.join(st)) #list -> string 출력
