from collections import deque

n,k = map(int,input().split())
graph = []
q = []


for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] !=0:
            q.append([graph[i][j], i,j, 0]) #바이러스번호, x좌표, y좌표, 걸린 시간
    
s, X, Y = map(int, input().split())

#l,u,r,d
dx = [0,-1,0,1]
dy = [1,0,-1,0]


q.sort() #1,2,3 순서대로 진행해야하므로 정렬!

queue = deque(q)

while queue:

    v, x, y, time = queue.popleft()
    if time == s:
        break
        
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx >=0 and nx<n and ny>=0 and ny<n: #ny<n을 k로 해놓고 계속 런타임오류나서 애먹었다,,, 조심하
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                queue.append([v,nx,ny, time +1])
            
            
print(graph[X-1][Y-1])


"""
처음에
바이러스 번호에 해당되는 리스트 인덱스에 리스트로 좌표를 추가하고
큐로 돌리면서 bfs로 세균들을 1,2,3... 순서로 증폭시킨뒤 시간 1씩 추가했는데
첫번째 턴을 돌고 그 다음턴으로 돌지를 못했다.

리스트 묶음에 [시간, 좌표, 바이러스번호] 이렇게 입력해보니
한번에 값을 입력하고 받아올 수 있어서 좋은 방법이었다.

이 문제를 풀면서 bfs에 대해 좀 더 이해할 수 있었던 것 같다!

"""
