def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    i = 0
    for a in A:
        if a < B[i]:
            answer += 1
            print(B[i])

            i += 1
    return answer


print(solution([5,1,3,7], [1,1,1,8]))