n, k = map(int, input().split())
money = []
answer = 0

for i in range(n):
    money.append(int(input()))

money.reverse()

for i in money:
    if k<i:
        continue

    else:
        answer += k//i
        k = k%i
        
print(answer)

"""
화폐입력을 내림차순 리스트로 받는다
일단 화폐단위가 계산할 돈보다 크면 pass
작으면 동전개수와 동전개수 계산하고 남은 가치의 합을 계속 구해나간다.
"""
