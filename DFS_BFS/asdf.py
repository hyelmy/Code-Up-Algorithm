from sys import stdin
from collections import deque

move = [[-1,0],[1,0],[0,-1],[0,1]]
N, K = map(int, stdin.readline().split())
board = [list(map(int,stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, stdin.readline().split())

q = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            q.append([board[i][j], i, j, 0])

q.sort()
q = deque(q)
X -= 1
Y -= 1

print(q)
