import itertools

n = int(input())
array = list(map(int,input().split()))

add, sub, mul, div = map(int,input().split())



min_value = 10**9
max_value = -10**9


def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        if add>0:
            add-=1
            dfs(i+1,now+array[i])
            add += 1
        if sub>0:
            sub-=1
            dfs(i+1,now-array[i])
            sub += 1
        if mul>0:
            mul-=1
            dfs(i+1,now*array[i])
            mul += 1
        if div>0:
            div-=1
            dfs(i+1, int(now/array[i]))
            div+=1

dfs(1, array[0])

print(max_value)
print(min_value)
"""
itertools를 사용할 수 있을 것 같아 해봤었는데 product로 할려니 똑같은 연산이 나왔을 때
쉽지 않았다.

어떤 사람은 permutation으로 해서 set으로 제거했네 천재인가
(https://inspirit941.tistory.com/102)

재귀로 푸는 방법이 더 단순하고 깔끔했다
재귀... 아직도 아리까리 하다

"""
