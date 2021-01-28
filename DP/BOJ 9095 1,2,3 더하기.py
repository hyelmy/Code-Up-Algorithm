n = int(input())
data= []
for i in range(n):
    data.append(int(input()))
dp=[1,2,4]

for i in range(3,max(data)):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for i in data:
    print(dp[i-1])
    
        
"""
dp문제니까 dp그래프를 토대로 거슬러 올라가야한다는 강박에 풀다가
순서가 중복되는 경우를 제대로 처리하지 못했다...

0에서부터 1,2,3씩 더해가며 나오는 수를 인덱스로 하여
1씩 더해가면 되는 문제였다...

아아...



이상한 코드....
n = int(input())

data = list(map(int, input().split()))

for i in data:  #리스트 돌리기
    dp = [0]*(i+1)
    dp[1] = 1
    cnt = 0
    for j in range(2, i+1):   #2부터 n까지 경우의 수 돌리기

        
        for k in range(1, j+1):#j의 경우의 수 구하기
            temp = j-k
            print("%d %d "%(temp, k)) 
            if temp == 0 and (k == 2 or k==3):<---여기서부터 코드가 이상
                dp[j]+=1

            elif temp == 1 or k == 1:
                dp[j] += max(dp[temp], dp[k])
            
            else:
                dp[j] += dp[temp]+dp[k]
            print(dp[j])
        print(dp)

    print(dp[i])


"""
