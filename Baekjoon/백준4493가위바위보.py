if __name__ == '__main__' :
    x=int(input())

    for i in range(x):
        n=int(input())

        p1=0 #player1
        p2=0 #player2
        for i in range(n):
            temp=input().split()
            if temp[0]=="R": #바위
                if temp[1]=="S":
                    p1+=1
                elif temp[1]=="P":
                    p2+=1
            elif temp[0]=="S": #가위
                if temp[1]=="R":
                    p2+=1
                elif temp[1]=="P":
                    p1+=1
            elif temp[0]=="P": #보
                if temp[1]=="R":
                    p1+=1
                elif temp[1]=="S":
                    p2+=1
        if(p1>p2):
            print("Player 1")
        elif (p1<p2):
            print("Player 2")
        else:
            print("TIE")
