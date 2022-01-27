import sys

if __name__=='__main__':
    n=int(input())
    arr=[0,0,0,0,0]
    for i in range(n):
        x,y=map(int, sys.stdin.readline().split())

        if x>0 and y>0: #1사분면
            arr[0]+=1
        elif x>0 and y<0: #4사분면
            arr[3]+=1
        elif x<0 and y>0: #2사분면
            arr[1]+=1
        elif x<0 and y<0: #3사분면
            arr[2]+=1
        else: #축
            arr[4]+=1

    print("Q1: "+str(arr[0]))
    print("Q2: " + str(arr[1]))
    print("Q3: " + str(arr[2]))
    print("Q4: " + str(arr[3]))
    print("AXIS: " + str(arr[4]))
