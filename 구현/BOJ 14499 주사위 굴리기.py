n,m ,x,y, k = map(int, input().split())


location = [list(map(int,list(input().split()))) for _ in range(n)]

command = list(map(int,input().split()))


dice = [0]*7


def move(a, x, y):
    if a ==1:
        nx = x
        ny = y+1
    elif a == 2:
        nx = x
        ny = y -1
    elif a ==3:
        nx = x-1
        ny = y
    else:
        nx = x+1
        ny = y
    return nx, ny

i = 0

for i in range(k):
    nx, ny = move(command[i], x, y)
  
    if nx < n and ny < m and nx >=0 and ny >=0:
        x = nx
        y = ny

        temp = dice.copy()
        #방향대로 굴리기(동,서,북,남)
        if command[i] ==1:
            dice[1] = temp[4]
            dice[3] = temp[1]
            dice[6] = temp[3]
            dice[4] = temp[6]

        elif command[i] ==2:
            dice[1] = temp[3]
            dice[6] = temp[4]
            dice[3] = temp[6]
            dice[4] = temp[1]

        elif command[i] ==3:
            dice[1] = temp[5]
            dice[5] = temp[6]
            dice[2] = temp[1]
            dice[6] = temp[2]

        elif command[i] == 4:
            dice[1] = temp[2]
            dice[2] = temp[6]
            dice[5] = temp[1]
            dice[6] = temp[5]
        
        if location[x][y] == 0:
            location[x][y] = dice[6]
        
            
        else:
            dice[6] = location[x][y]
            location[x][y] = 0

        print(dice[1])

        
    else:
        continue
    i+=1
"""
시뮬레이션은 문제를 그대로 구현해내는 게 중요한 것 같다.
주사위가 굴려질때마다 가리키는 방향이 달라지는 것이 핵심 포인트!

주사위 방향이 바뀌는 부분에서 너무 복잡하게 생각해서 잘 풀리지 않았다..
그래도 잘 풀었다!
"""
