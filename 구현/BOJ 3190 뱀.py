n = int(input())
k = int(input())

array = [[0]*n for _ in range(n)]
direction = []

for i in range(k):      #사과가 있는 좌표의 값을 5로 변경
    a,b = map(int, input().split())
    array[a-1][b-1] = 5

l = int(input())
for j in range(l):      #뱀의 방향 변환 정보를 리스트에 담음
    a,b = input().split()
    direction.append((int(a),b))



#동, 남, 서, 북 (오른쪽으로 회전하면 +1씩, 왼쪽으로 회전하면 -1 하면 된다)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

x=0	#뱀 머리(제일 맨 앞)의 현재 x,y 좌표
y=0

dir = 0	#dx, dy 조작할 변수
cnt = 0	#시간 잴 변수
index = 0   #방향 변환 정보(direction) 조작할 변수
array[0][0] = 1	#뱀의 초기 위치 지정


q = [(x,y)] #뱀이 차지하고 있는 위치 정보
while(True):
    nx = x + dx[dir]    #방향대로 1칸씩 이동시킴
    ny = y + dy[dir]
    
    
    if nx >=0 and nx < n and ny >=0 and ny <n and array[nx][ny] != 1:   #맵의 범위 안에 있고, 뱀의 몸통이 없는 위치일 때

        if array[nx][ny] == 5:  #사과가 있으면
            array[nx][ny] = 1	#이동 후 꼬리 그대로 두기
            q.append((nx,ny))

        else:                   #사과가 없을 때
            array[nx][ny] = 1	#이동 후 꼬리 제거
            q.append((nx,ny))
            px, py = q.pop(0)   
            array[px][py] = 0
        
    else:               #맵의 범위를 벗어나거나 몸통과 부딪혔을 때 break
        cnt+=1
        break
    x = nx	        #현재 뱀의 머리 위치 조정, 시간 count +1
    y = ny
    cnt+=1


    if index < len(direction) and cnt == direction[index][0]:   #만약 시간이 방향 변환 정보 시간과 일치할 경우 회전시킴
        if direction[index][1] == 'L':     #왼쪽
            dir -= 1
            if dir == -1:
                dir = 3
            
            
        elif direction[index][1] == 'D':   #오른쪽
            dir +=1
            if dir == 4:
                dir = 0
        index +=1

    

print(cnt)
"""
방향 변환 횟수 리스트로 돌려서 한번에 이동시키려다가 실패 -> 매 초마다 계산해야 뱀의 방향바꾸는 타이밍을 알 수 있기 때문(애초에 잘못된 방식이었다)

뱀의 몸통이 있는 위치를 확인 하는 방법에서 어려웠다.
그 방법의 결과 q에 뱀이 이동하는 좌표를 넣고 사과가 없는 경우
맨 첫번째 좌표(꼬리값<- 계속 뒤로 뱀의 새로운 좌표를 집어넣기 때문)를 꺼내서 값을 바꿔 꼬리를 제거하게끔하면 됐다!

구현 처음으로 제대로 풀었다!!(좀 오래 걸렸지만...)

더 노력하자!!!

"""
