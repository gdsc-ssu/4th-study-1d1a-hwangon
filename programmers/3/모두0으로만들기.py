import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

result = 0
def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    
    def dfs(child, parent):
        global result
        for c in graph[child]:
            if c != parent:
                dfs(c, child)
        
        a[parent] += a[child]
        result += abs(a[child]) 


    dfs(0, 0)
    return result


print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))