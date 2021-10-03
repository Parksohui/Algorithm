import sys

if __name__=='__main__':
    n=int(sys.stdin.readline().strip()) # 피연산자의 개수

    line=sys.stdin.readline().strip() # 후위 표기식
    num=[] #  피연산자 대응하는 값 넣을 배열
    dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
            'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
            'Z': 25} # 피연산자_index match

    for i in range(n): # 피연산자 대응하는 값
        num.append(int(sys.stdin.readline().strip()))

    arr=[] # 수식
    for i in line:
        if i.isalpha(): # 영대문자면 숫자로 바꿔 넣음
            arr.append(num[dict[i]])
        else: # 연산자
            b=arr.pop()
            a=arr.pop()
            if i=='+': # 더하기
                arr.append(a+b)
            elif i=='-': # 빼기
                arr.append(a-b)
            elif i=='*': # 곱하기
                arr.append(a*b)
            elif i=='/': # 나누기
                arr.append(a/b)

    print("{:.2f}".format(arr[-1])) # 소숫점 둘째 자리까지 출력
