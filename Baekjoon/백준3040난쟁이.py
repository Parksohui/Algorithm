from itertools import combinations

if __name__=='__main__' :
    num=[]
    for i in range(9):
        num.append(int(input()))

    arr = list(combinations(num, 7)) #순서 상관 x_조합

    result=[]
    for i in arr:
        if sum(i)==100: #합이 100이면
            result=i
            break

    for i in result:
        print(i)
