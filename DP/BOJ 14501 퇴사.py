n = int(input())
t = [] #상담 완료하는데 걸리는 시간만
p = [] #상담 완료 했을 때 받는 금액
dp = [0]*(n+1)  #dp[i] = i일부터 퇴사 날까지 얻을 수 있는 최대 이익
max_value = 0

for _ in range(n):
    x,y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1,-1):
    time = t[i]+i    #i번째 날이 상담 가능한 날짜 범위에서 넘어가는지 확인, time -> i번째날 상담 완료하는데 걸리는 시간 + i번째날
                    

    if time <= n:    #넘어가지 않을 경우
        dp[i] = max(p[i] +dp[time], max_value)  #현재 상담 일자의 이윤(p[i])+ 현재 상담을 마친 일자부터 최대이윤(dp[t[i]+i]) 계산해서 최댓값 저장
                                                #i번째 날부터 퇴사날(n)까지 얻을 수 있는 
        print(p[i] + dp[time])
        print(max_value)
        print(dp)
        max_value = dp[i]
    else:               #넘어가는경우
        dp[i] = max_value #현재까지의 최대 금액 유지
print(max_value)


"""
-틀린 이유

징검다리로 꼭 상담끝난 날짜로 이동하는게 아니라
그 이후는 어떤 날짜든 상담할 수 있는 거였다.

예제 4로 예시를 들면
1 -> 6 -> 8 이 정답인데 이유는
1번 5, 50
6번 1,10 까지 이동을 했을 때, 더 많은 이익을 가져가기 위해서
7번 1,10 이 아닌
8번 3, 30으로 가야하는 것이다.

즉, 더 많은 이익을 취하기 위해 바로 그 다음 날짜가 아닌 더 이익을 취할 수 있는
날짜로 건널 수 있던 것이다.

그리고 8+3이 11인데 되는 이유는 8일부터 시작된다고 하면
8,9,10 으로 실은 10일에 끝나는 것이기 때문에 가능하다.

징검다리처럼 건너건너만 가야한다고 생각해서 처음부터 잘 못 짠 것 같다...
그리고 그리디 이용해야했는데 그리디도 사용안했다ㅠ

N+1(<=n)인 이유는 상담이 걸리는 시간이 상담을 시작한 날을 포함하기 때문이다.
예를 들어, 예제 4에서 i=8일 때 T [8]=3이다.
i+T [i](3+8)=11인데 사실은 10일에 끝나기 때문에 i + T [i] < N+1을 검사해주는 것이다.


"""

#예제 4에서 정답이 나오지 않은 풀이
"""
n = int(input())
t = []
for i in range(n):
    t.append(list(map(int,input().split())))

answer = 0
i = 0

while(i<n):

    s_cnt = t[i][0]
    s_money = t[i][1]


    j = i+ s_cnt
    if j> n-1:
        s_cnt = 0
        s_money = 0


    while(j < n and s_cnt + t[j][0] <=n):
        if j+t[j][0] >= n+1:
            break

        else:
            s_cnt += t[j][0]
            s_money += t[j][1]
            j += t[j][0] #00일차


    i+=1
    answer = max(answer, s_money)
print(answer)
"""
