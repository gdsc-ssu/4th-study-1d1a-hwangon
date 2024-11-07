from collections import Counter

def solution(a):
    elements = Counter(a)
    answer = -1

    # 모든 원소를 공통인자로 확인해본다
    for k in elements.keys():
        # 해당 원소 개수가 이전에 계산한 스타수열의 길이 이하라면 계산하지 않는다
        if elements[k] <= answer:
            continue

        common_cnt = 0
        idx = 0

        while idx < len(a) - 1:
            if(a[idx] != k and a[idx + 1] != k) or a[idx] == a[idx + 1]:
                idx += 1
                continue
                
            common_cnt += 1
            idx += 2

        answer = max(common_cnt, answer)

    if answer == -1:
        return 0
    else:
        return answer * 2
    

print(solution([5,2,3,3,5,3]))