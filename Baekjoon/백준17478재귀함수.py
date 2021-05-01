
if __name__=='__main__':
    a=int(input())

    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

    x="\"재귀함수가 뭔가요?\""
    y="\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
    z="마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
    w="그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""

    final="라고 답변하였지."

    print(x)
    print(y)
    print(z)
    print(w)

    blank="_"
    for i in range(1,a): #공백 
        print(blank * 4 * i + x)
        print(blank * 4 * i + y)
        print(blank * 4 * i + z)
        print(blank * 4 * i + w)

    print(blank * 4 * a + x)
    print(blank * 4 * a + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
    print(blank * 4 * a + "라고 답변하였지.")

    for i in range(a-1,0,-1): #거꾸로
        print(blank * 4 * i + final)

    print(final)