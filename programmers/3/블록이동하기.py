from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def can_move(c1, c2, new_board):
    x, y = 0, 1
    cand = []

    for i in range(4):
        nxt1 = (c1[x] + dx[i], c1[y] + dy[i])
        nxt2 = (c2[x] + dx[i], c2[y] + dy[i])
        if new_board[nxt1[x]][nxt1[y]] == 0 and new_board[nxt1[x]][nxt1[y]] == 0:
            cand.append((nxt1, nxt2))

    # 가로 방향일 때 회전
    if c1[x] == c1[y]:
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            if new_board[c1[x] + d][c1[y]] == 0 and new_board[c2[x] + d][c2[y]] == 0:
                cand.append((c1, (c1[x] + d, c1[y])))
                cand.append((c2, (c2[x] + d, c2[y])))
    # 세로 방향일 때 회전
    else:
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if new_board[c1[x]][c1[y] + d] == 0 and new_board[c2[x]][c2[y] + d] == 0:
                cand.append(((c1[x], c1[y] + d), c1))
                cand.append(((c2[x], c2[y] + d), c2))
    
    return cand


def solution(board):
    answer = 0
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    
    q = deque([((1, 1), (1, 2), 0)])
    confirm = set([((1, 1), (1, 2))])

    while q:
        c1, c2, count = q.popleft()
        if c1 == (n, n) or c2 == (n, n):
            return count
        for nxt in can_move(c1, c2, new_board):
            if nxt not in confirm:
                q.append((*nxt, count + 1))
                confirm.add(nxt)


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))