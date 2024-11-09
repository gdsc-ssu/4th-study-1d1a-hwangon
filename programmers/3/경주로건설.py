from collections import deque

INF = 1e9

def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(start):
        n = len(board)
        visited = [[INF] * n for _ in range(n)]
        visited[0][0] = 0

        q = deque([start])

        while q:
            x, y, direction, cost = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                    if i == direction:
                        ncost = cost + 100
                    else:
                        ncost = cost + 600

                    if ncost < visited[nx][ny]:
                        visited[nx][ny] = ncost
                        q.append([nx, ny, i, ncost])
        
        return visited[-1][-1]
    
    return min(bfs((0, 0, 1, 0)), bfs((0, 0, 3, 0)))


print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))