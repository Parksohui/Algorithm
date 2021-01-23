if __name__ == '__main__':
    A,B=input().split(" ")

    result=str(int(A[::-1])+int(B[::-1]))
    print(int(result[::-1]))
