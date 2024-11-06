import heapq
from collections import defaultdict

def solution(n, s, a, b, fares):
    INF = 1e9
    answer = INF
    graph = defaultdict(list)

    for f in fares:
        node1, node2, fee = f
        graph[node1].append((node2, fee))
        graph[node2].append((node1, fee))
    
    def dijkstra(s):
        q = []
        distance = [INF] * (n + 1)
        heapq.heappush(q, (0, s))
        distance[s] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue

            for g in graph[now]:
                cost = dist + g[1]
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
                    heapq.heappush(q, (cost, g[0]))
            
        return distance
    
    distance_list = [[]] + [dijkstra(i) for i in range(1, n + 1)]

    for i in range(1, n + 1):
        answer = min(distance_list[s][i] + distance_list[i][a] + distance_list[i][b], answer)

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))