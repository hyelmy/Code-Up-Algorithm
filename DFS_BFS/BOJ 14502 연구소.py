import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = 0
data = []
temp = [[0] * m for _ in range(n)]
for i in range(n):
    data.append(list(map(int, input().split())))


#L, U, R, D
dx = [0,-1,0,1]
dy = [1,0,-1,0]

#바이러스가 사방으로 퍼지도록하는 함수
def spread_virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y +dy[i]

        if nx>=0 and nx<n and ny >= 0 and ny<m: #영역 안으로만 확인
            if temp[nx][ny] == 0: #바이러스가 퍼지지않은 안전구역이면
                temp[nx][ny] = 2 #전염시키기
                spread_virus(nx, ny)
                
#안전 구역이 몇개인지 확인하는 함수
def get_score(): 
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0: #0일때(안전구역)마다 count += 1
                score +=1
    return score

def dfs(count):
    global result
    if count == 3:          #울타리를 3개 지었을 경우
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j] #temp에 data를 copy
                #이 과정은
                #import copy
                #temp = copy.deepcopy(data)로도 가능하다
                
        for i in range(n):
            for j in range(m):
                if temp[i][j] ==2: #바이러스가 있을 경
                    spread_virus(i,j) #바이러스를 퍼뜨린후 
        result = max(result, get_score()) #안전구역 개수 계산
        print(result)
        return
    
    for i in range(n): #빈 공간에 울타리  설치
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
            
                count += 1 # 설치할 때마다 count +=1 (3개까지만 설치)
                print(str(i)+str(j)+"에 벽 건설")
                print("dfs 호출")
                dfs(count)
                print("dfs 전으로 돌아옴")
                data[i][j] = 0 #최근에 세운 벽 초기화
                print(str(i)+str(j)+"에 벽 초기화")
                count -= 1
dfs(0)
print(result)


"""
쉽게 풀어쓴 풀이 설명
https://hyelmy.github.io


"""
