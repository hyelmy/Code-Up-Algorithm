n ,m = map(int,input().split())
mapp = []


x, y, direction = (map(int, input().split())) #0,1: 위치, 2:방향

#1이 바다, 0이 육지
for i in range(n):
    mapp.append(list(map(int, input().split())))

#북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turnLeft(): #왼쪽으로 뱡향 돌리기(중복적이므로 함수로 따로 빼기)
    global direction
    direction -= 1
    if direction == -1: #이 과정을 하지 않으면 list 범위 초과 뜸
        direction = 3

cnt = 1
turntime = 0 #1. 방향 돌린 횟수 체크 (4까지 늘어나면 모든 방향 다 체크한 것임) 
mapp[x][y] = 1

while(True):
    turnLeft()  #왼쪽으로 방향 돌리기

    nx = x+dx[direction]    #방향 돌리고 위치 임시 변경
    ny = y+dy[direction]

    if mapp[nx][ny] == 0:   #2. 방향 돌린 곳이 가보지 않은 육지이면, 이동
        mapp[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turntime = 0    #방향 체크 초기화
        continue
            
    else:
        turntime += 1   #방향 체크 1 증가시키기

    if turntime == 4:   #3. 방향 체크가 4이면 동서남북 4방향 다 확인했기 때문에 
        nx = x - dx[direction]  #바라보는 방향으로 1칸씩 돌아가기
        ny = y - dx[direction]

        if mapp[nx][ny] == 0:   #뒤쪽이 바다칸이면 break
            x =nx
            y = ny
        else:
            break
        turntime = 0

print(cnt)

"""
방향을 돌릴 때 for i in range(4)로 할려고했다가 잘 안됐다.

"""
