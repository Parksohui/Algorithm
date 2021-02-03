if __name__=='__main__' :
    x=list(input())

    count=0

    idx=0

    while(len(x)!=0):
        if len(x)-1>idx :
            if x[idx]=='c' and x[idx+1]=='=': #'c='
                count+=1
                x.pop(0)
                x.pop(0)
            elif x[idx]=='c' and x[idx+1]=='-': #'c-'
                count+=1
                x.pop(0)
                x.pop(0)
            elif x[idx]=='d' and x[idx+1]=='-': #'dz='
                count+=1
                x.pop(0)
                x.pop(0)
            elif x[idx]=='l' and x[idx+1]=='j': #'d-'
                count+=1
                x.pop(0)
                x.pop(0)
            elif x[idx]=='n' and x[idx+1]=='j': #'lj'
                count+=1
                x.pop(0)
                x.pop(0)
            elif x[idx]=='s' and x[idx+1]=='=': #'nj'
                count+=1
                x.pop(0)
                x.pop(0)
            elif x[idx]=='z' and x[idx+1]=='=': # z='
                count+=1
                x.pop(0)
                x.pop(0)
            elif len(x) - 2 > idx:
                if x[idx] == 'd' and x[idx + 1] == 'z' and x[idx + 2] == '=': #'dz='
                    count += 1
                    x.pop(0)
                    x.pop(0)
                    x.pop(0)
                else:
                    count += 1
                    x.pop(0)
            else:
                count += 1
                x.pop(0)
        else:
            count+=1
            x.pop(0)

    print(count)