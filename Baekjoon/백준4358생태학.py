import sys

if __name__=='__main__':
    tree={}
    cnt=0

    while True:
        x=sys.stdin.readline().rstrip() 

        if not x: # 입력 끝
            break
        if x not in tree: # key값이 없으면 
            tree[x]=1
        else: # key값이 있으면
            tree[x]+=1
        cnt += 1 # 총 나무 수

    tree=sorted(tree.items()) # 사전순 정렬

    for i in tree: # 소수점 4째자리까지 반올림해서 출력
        print(i[0]+' %.4f' %(i[1]/cnt *100))
