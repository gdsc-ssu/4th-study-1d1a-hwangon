def solution(stones, k):
    left = 1
    right = 1e9

    while left <= right:
        mid = (left + right) // 2
        cnt = 0

        for t in stones:
            # 뛰어 넘어야하는 돌의 수
            if t - mid <= 0:
                cnt += 1
            # 넘지 않아도 되는 돌이 생기면 초기화
            else:
                cnt = 0

            if cnt >= k:
                break
        
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))