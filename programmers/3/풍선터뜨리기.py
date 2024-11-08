INF = 1e9

def solution(a):
    result = [False] * len(a)
    min_front = INF
    min_back = INF

    for i in range(len(a)):
        if a[i] < min_front:
            min_front = a[i]
            result[i] = True
        if a[-1 - i] < min_back:
            min_back = a[-1 - i]
            result[-1 - i] = True

    return sum(result)


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))