from itertools import permutations
import re

def solution(user_id, banned_id):
    answer = set()
    n = len(banned_id)
    perm = list(permutations(user_id, n))

    for p in perm:
        count = 0
        for i in range(n):
            if not re.match(banned_id[i].replace('*', '.'), p[i]) or len(banned_id[i]) != len(p[i]):
                break
            else:
                count += 1
        
        if count == n:
            answer.add(p)

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))