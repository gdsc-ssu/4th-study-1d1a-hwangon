import heapq
from collections import defaultdict

INF = 1e9

def solution(n, edge):
    answer = 0

    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0

    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    max_dist = max(distance[1:])
    for i in distance:
        if i == max_dist:
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))