n,m = map(int,input().split())

a = []
b = []
for i in range(n):
    a.append(list(map(int, input())))

for j in range(n):
    b.append(list(map(int, input())))

cnt = 0
answer = 1
for i in range(n-2):    
    for j in range(m-2):
        if a[i][j] != b[i][j]: #a,b가 다를 경우
            cnt += 1
            for k in range(i, i+3): #3x3 바꿔주기
                for l in range(j,j+3):
                    a[k][l] = 1 - a[k][l]
        else:
            continue
            
for i in range(n):
    if a[i] != b[i]:
        print(-1)
        answer = -1
        break

if answer == 1:
    print(cnt)

"""
이 문제의 핵심은 3x3으로 뒤집은 다음, 다음 인덱스로 넘어갈 때 변하지 않는 값이 있다는 것을 명심해야한다!
그것은 바로 (0,0)!

1111
1111
1111
↓1번째 뒤집기
0001
0001
0001
↓2번째 뒤집기
0110
0110
0110

여기서 보면 (0,0) 맨위, 맨 왼쪽 부분은 전혀 바뀌지 않는 것을 볼 수 있다.
((1,0),(2,0)은 세로로 더 길 경우 아래로 내려가서 (1,0)부터 3X3 뒤집을 때 다시 바뀐다.)

이러한 부분을 노리고 (0,0)같이 바뀌지않는 부분을 계속 늘려가는 것이다!

11111
11111
11111
11111
↓1번째 뒤집기
00011
00011
00011
11111
↓2번째 뒤집기
01101
01101
01101
11111
↓3번째 뒤집기
01010
01010
01010
11111
지금 상태에서는 (0,0),(0,1)이 앞으로 전혀 바뀌지않는 값이 되어있는 것이다!
3X3씩 다 뒤집어 준 뒤 만들어야할 B행렬과 비교하여
다른 요소가 있으면 -1 같으면 3X3 뒤집은 횟수를 출력하면 된다!

처음으로 아이디어가 제대로 맞은 문제다!
점점 늘고있다 화이팅!!!

간단 풀이
https://hyelmy.github.io
"""
