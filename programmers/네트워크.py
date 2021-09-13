def visit(i, computers, visited):
    visited[i] = True  # 방문
    for j in range(len(computers)):
        if computers[i][j] == 1 and visited[j] == False:  # 연결 되어있으며 방문한 적인 없다면
            visit(j, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]  # 초기화
    for i in range(n):
        if visited[i] == False:  # 아직 방문한 적이 없다면
            visit(i, computers, visited)  # 방문
            answer += 1  # 네트워크
    return answer