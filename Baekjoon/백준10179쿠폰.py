if __name__ == '__main__' :
    x=int(input())

    for i in range(x):
        y=float(input())
        print('$'+str(format(round(y*0.8,2),".2f")))