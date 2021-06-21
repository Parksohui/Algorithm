if __name__=='__main__':
    a=int(input())

    arr=[]
    for i in range(a):
        s=input()
        number=''
        for j in range(len(s)):
            if s[j].isdigit(): #숫자이면
                number+=s[j]
                if j==len(s)-1: #마지막 자리이면
                    arr.append(int(number))
            else: #문자이면
                if number!='' : #숫자 추가
                    arr.append(int(number))
                    number = ''
    arr.sort()
    for i in arr:
        print(i)
