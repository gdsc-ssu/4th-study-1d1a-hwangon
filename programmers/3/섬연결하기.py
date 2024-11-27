def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]


def union_paret(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    answer = 0

    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    costs = sorted(costs, key=lambda x: x[2])
    for a, b, cost in costs:
        if find_parent(parent, a) != find_parent(parent, b):
            union_paret(parent, a, b)
            answer += cost
        
    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))