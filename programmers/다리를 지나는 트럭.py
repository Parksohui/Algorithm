def solution(bridge_length, weight, truck_weights):
    answer = 1

    temp = []
    truck_weights.sort()
    temp.append(truck_weights.pop())

    while True:
        if (len(temp) == 0):
            answer += bridge_length - 1

            if (len(truck_weights) == 0):
                break
            else:
                temp.append(truck_weights.pop())

        if truck_weights:
            if (sum(temp) + truck_weights[0] < weight):
                temp.append(truck_weights.pop(0))
                answer += 1
            else:
                temp.pop(0)
        else:
            temp.pop(0)

    # answer+=bridge_length

    return answer + 1