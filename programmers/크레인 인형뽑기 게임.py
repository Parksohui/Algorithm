def solution(board, moves):
    answer = 0
    result = []

    for i in moves:
        for j in range(len(board)):
            if (board[j][i - 1] != 0):  # 인형이 있는 곳 확인
                if (len(result) != 0 and result[-1] == board[j][i - 1]):  # 인형이 터트려질때
                    result.pop()
                    answer += 2
                    board[j][i - 1] = 0
                else:  # 안터트려지고 바구니에 쌓일때
                    result.append(board[j][i - 1])
                    board[j][i - 1] = 0
                break

    return answer