
def solution(bridge_length, weight, truck_weights):

    answer =0
    temp =[0 ] *bridge_length  # 다리 길이만큼 리스트 선언


    while(temp):
        temp.pop(0)  # 앞으로 한칸씩 당겨짐
        if len(truck_weights ) >0:  # 트럭이 남아있으면
            if sum(temp ) +truck_weights[0 ]<=weight:  # 무게를 견딘다면
                temp.append(truck_weights.pop(0))  # 다리에 올라감
            else:  # 무게를 못견딘다면
                temp.append(0)  # 다리에 있는 트럭 마저 지나가도록

        answer +=1  # 1초 지남


    return answer