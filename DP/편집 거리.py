a = input()
b= input()

n = len(a)
m = len(b)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][0] = i
for j in range(1,m+1):
    dp[0][j] = j


for i in range(1, n+1):
    for j in range(1,m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 +min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    
print(dp[n][m])
"""
처음엔 dp를 사용하지 않았다.(아래의 이상한 코드....)
이렇게 하다보니 계속 최소편집거리를 구해야하는데, 첫 편집거리 경우의 수 한가지밖에 구할 수 없었다.

점화식:
두 문자가 같은 경우 : dp[i][j] = dp[i-1][j-1](행과 열에 해당하는 문자가 서로 같다면, 왼쪽 위에 해당하는 수 그대로 대입)
두 문자가 다른 경우 : dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) (행과 열에 해당하는 문자가 서로 다르다면, 왼쪽(삽입), 위쪽(삭제), 왼쪽 위(교체)에 해당한느 수 중에서 가장 작은 수 1을 더해 대입)

dp는 정말 점화식을 잘 구해야하는 것 같다...
더 연습하자...!!!

ex)
sunday
saturday
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[1, 0, 1, 2, 3, 4, 5, 6, 7]
[2, 1, 1, 2, 2, 3, 4, 5, 6]
[3, 2, 2, 2, 3, 3, 4, 5, 6]
[4, 3, 3, 3, 3, 4, 3, 4, 5]
[5, 4, 3, 4, 4, 4, 4, 3, 4]
[6, 5, 4, 4, 5, 5, 5, 4, 3]


----------------------------------------------------------------
answer = 0
cnt = 0


for i in range(len(a)):
    n = i
    print(a[i])
    for j in range(n, len(b)):
        print(b[j])
        if a[i] == b[j]:
            print("똑같은 거 발견!")
            print(cnt)
            answer += cnt
            print("answer = "+str(answer))
            n = cnt+2
            cnt = 0
            break

        else:
            if j == len(a)-1:
                print("끝까지 찾아봤지만 없음")
                cnt = 1
                
                break
            
            else:
                print("똑같은 요소가 아님")
                cnt+=1
                print(cnt)
                
        
print(answer)
"""
