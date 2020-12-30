from collections import deque
import sys
#도시 개수 n, 도로개수 m, 거리정보 k, 출발도시 x

def bfs(graph,k,x, visited):
    queue = deque([x])
    while(queue):
        
        v = queue.popleft()

        for i in graph[v]:
            
            if visited[i]== -1:
                visited[i] = visited[v] +1
                queue.append(i)
                
                
    check = False
    for i in range(1, n+1):
        if visited[i] ==k:
            print(i)
            check = True
    if check == False:
        print(-1)
        
input = sys.stdin.readline
        
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = (map(int,input().split()))
    graph[a].append(b)

visited = [-1]*(n+1)
visited[x] = 0

bfs(graph, k,x, visited)

"""
input = sys.stdin.readline 해야 런타임 초과가 안남!

리스트 길이 조심하자... 저 n+1을 n으로 해서 계속 오류난 것이었다,,,!ㅠㅠ
결과를 받아서 출력하는것이 더 좋은듯!
경우의 수가 있을 때마다 그때 그때 출력하려고 하니까 더 복잡해졌던 것 같다


"""
