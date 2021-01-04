n,m = map(int, input().split())
array = []

for i in range(n):
    array.append(int(input()))

d = [10001]*(m+1)

d[0] = 0

for i in range(n):                  #0~n -> 화폐개수
    for j in range(array[i], m+1):  #array[i]~m -> 첫 화폐단위부터 만들어야할 숫자까
        if d[j-array[i]] != 10001:
             d[j] = min(d[j], d[j-array[i]]+1)

if d[m]==10001:
    print(-1)

else:
    print(d[m])
        
"""
j가 1~m원 까지 돌면서
각각의 원을 만들 수 있는지 check

j-k를 만들 수 있다면
j도 만들 수 있다!

** 이전에 구한 데이터를 사용하여 현재의 데이터를 구할 수 있다는 것이 DP의 핵심임을 잊지말자!

"""
