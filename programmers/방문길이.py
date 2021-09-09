def solution(dirs):
    answer = 0

    x, y = 0, 0
    arr = set()

    for i in dirs:  # U,D,R,L
        start_x, start_y = x, y  # 시작 위치 update
        if i == 'U' and y < 5:
            y += 1
        elif i == 'D' and y > -5:
            y -= 1
        elif i == 'R' and x < 5:
            x += 1
        elif i == 'L' and x > -5:
            x -= 1

        if start_x == x and start_y == y:  # 좌표를 벗어나 같은 자리에 머물면
            pass
        else:  # 양방향으로 넣어줌
            arr.add((start_x, start_y, x, y))
            arr.add((x, y, start_x, start_y))

    answer = len(arr) // 2  # 양방향으로 저장했으므로 나누기 2

    return answer