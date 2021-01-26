if __name__ == '__main__' :
    x=input()
    while(x!='0'): #0이 아닐때 판별
        temp=x[::-1] #뒤집기
        if(x==temp): #같으면 팰린드롬
            print("yes")
        else:
            print("no")
        x = input()

