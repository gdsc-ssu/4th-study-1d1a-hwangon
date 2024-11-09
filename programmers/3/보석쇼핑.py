def solution(gems):
    n = len(gems)
    answer = [0, n - 1]
    kind = len(set(gems))
    
    gem_dic = {}
    gem_dic[gems[0]] = 1

    s, e = 0, 0
    while s < n and e < n:
        # 보석 개수가 부족하면 e 포인터 이동
        if len(gem_dic) < kind:
            e += 1
            if e == n:
                break
            gem_dic[gems[e]] = gem_dic.get(gems[e], 0) + 1
        else:
            # 정답 갱신
            if (e - s + 1) < (answer[1] - answer[0] + 1):
                answer = [s, e]
            
            # s 포인터 값 삭제 후 이동
            if gem_dic[gems[s]] == 1:
                del gem_dic[gems[s]]
            else:
                gem_dic[gems[s]] -= 1
            
            s += 1

    answer[0] += 1
    answer[1] += 1

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))