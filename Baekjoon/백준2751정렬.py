# version 1
if __name__=='__main__' :
    N=int(input())

    arr=[]
    for i in range(N):
        arr.append(int(input()))

    arr.sort()

    for i in arr:
        print(i)

# version2

# if __name__=='__main__' :
#     N=int(input())
#
#     arr=[]
#     for i in range(N):
#         arr.append(int(input()))
#
#     result=sorted(arr)
#
#     for i in result:
#         print(i)

