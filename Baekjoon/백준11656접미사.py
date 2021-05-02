if __name__=='__main__':
    a=input()

    arr=[]

    for i in range(len(a)):
        arr.append(a[i::])

    arr.sort() #정렬

    for i in arr:
        print(i)

