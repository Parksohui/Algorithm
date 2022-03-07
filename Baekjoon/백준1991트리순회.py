import sys

def preorder(n,tree,answer): #전위 순회
    if n!='.':
        answer.append(n)
        if tree[n][0]!='.': 
            preorder(tree[n][0],tree,answer)
        if tree[n][1]!='.':
            preorder(tree[n][1],tree,answer)

def inorder(n,tree,answer): #중위 순회
    if n!='.':
        if tree[n][0]!='.':
            inorder(tree[n][0],tree,answer)
        answer.append(n)
        if tree[n][1]!='.':
            inorder(tree[n][1],tree,answer)

def postorder(n,tree,answer): #후위 순회
    if n!='.':
        if tree[n][0]!='.':
            postorder(tree[n][0],tree,answer)
        if tree[n][1] != '.':
            postorder(tree[n][1], tree, answer)
        answer.append(n)

if __name__=='__main__':
    n=int(input())
    tree={}

    for i in range(n):
        temp=sys.stdin.readline().split()
        tree[temp[0]]=[temp[1],temp[2]]

    answer=[]
    #전위 순회
    preorder('A', tree, answer)
    print(''.join(answer))

    answer=[]
    #중위 순회
    inorder('A',tree,answer)
    print(''.join(answer))

    answer=[]
    #후위 순회
    postorder('A',tree,answer)
    print(''.join(answer))