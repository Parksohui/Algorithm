import sys
if __name__=='__main__':
    N,M=map(int,sys.stdin.readline().split())
    num,name=sys.stdin.readline().split()

    a={}
    b={}
    while num!='0' and name!='0':
        if int(num)%2==1: # 청
            if int(num) not in a: # 추가
                a[int(num)]=[name]
            else:
                temp=a[int(num)]
                if len(temp) < M: # 선착순
                    temp.append(name)
                    a[int(num)]=temp
        else: # 백
            if int(num) not in b: # 추가
                b[int(num)]=[name]
            else:
                temp =b[int(num)]
                if len(temp)<M: # 선착순
                    temp.append(name)
                    b[int(num)]=temp
        num, name = sys.stdin.readline().split() # 입력

    if len(a)!=0:
        a=sorted(a.items())
        for i in a:
            temp = i[1]
            temp.sort(key=lambda x: len(x))
            for j in temp:
                print(i[0], j)
    if len(b)!=0:
        b=sorted(b.items())
        for i in b:
            temp=i[1]
            temp.sort(key=lambda x: (len(x),x))
            for j in temp:
                print(i[0],j)