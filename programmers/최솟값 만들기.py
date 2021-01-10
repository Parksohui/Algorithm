def solution(A, B):
    answer = 0

    A.sort()
    B.sort()
    for i in range(len(A)):
        answer += A[i] * B[len(B) - 1 - i]  # A의 최솟값 * B의 최댓값

    return answer