from itertools import permutations

if __name__=='__main__' :
    N=int(input())

    nums=[i for i in range(1,N+1)]
    arr=list(permutations(nums,N)) #순열

    for i in arr:
        print(' '.join(map(str,i)))
