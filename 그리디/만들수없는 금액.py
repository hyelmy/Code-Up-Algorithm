n = map(int, input().split())

data = list(map(int, input().split()))

data.sort()


target = 1
for x in data:
    if target<x:
        break
    target += x

print(target)


"""
그리디의 개념을 정확히 이해하게된 문제였다.
현재 상태에서 매번 가장 좋아보이는 것만 선택하는 것 -> 그리디

나는 현재상태에서 매번 가장 좋아보이는 것이 아니라
처음부터 하나하나 경우를 다 따져가며 하려했다.

해당 화폐로 부터 만들 수 있는 모든 합을 구하고
이를 중복없게 set으로 만들어서 1부터 없는 수를 찾으려는
너무 비효율적인 방법으으로 하려했다.

앞으로는 이런 실수 하지 않기!!

answer = set(data)


for i in range(len(data)):
    for j in range(i+1, len(data)):
        answer.add(data[i]+data[j])

print(answer)

a = 1

while(True):
    print(a)
    if a not in answer:
        print(a)
        break
    a += 1
"""
