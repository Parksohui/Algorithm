def solution(arr):
    del arr[arr.index(min(arr))]  # 가장 작은 수 제거

    if (len(arr) == 0):
        arr.append(-1)
    return arr