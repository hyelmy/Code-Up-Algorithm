num = int(input())
time = []

for i in range(num):
    fir, sec = map(int, input().split())
    time.append([fir,sec])

    
print(time)
time = sorted(time, key=lambda x:x[1])
print(time)
time = sorted(time, key=lambda x:x[0]) // -> 두가지 정렬을 time = sorted(time, key = lambda x:(x[1], x[0]))로 합칠 수 있음
print(time)

last = 0
answer = 0

for i, j in time:
    if i>= last:
        answer += 1
        last = j
print(answer)



"""
회의가 겹치지 않으면서 최대 수를 구해야한다.
문제에서

"단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다."

라고 되어있는데 빨리끝나는 회의 순서대로 정렬해야함(빨리끝날 수록 고려해볼 회의 많기 때문), 시작시간 == 끝나는 시간일 경우, 끝나는 시간이 같을경우 빨리 시작하는 순서대로 정렬을 따져야한다

이때 조심해야할 부분! 시작시간의 오름차순 정렬 -> 정렬된 리스트 다시 끝나는 시간으로 오름차순으로 정렬해주어야한다.
이 때, 왜 굳이 두번 정렬을 해야하나요? 그냥 끝나는 시간으로 오름차순하면 되는거 아닌가요? 할 수 있는데,

예시를 보면 출력 결과물이 다르게 나온다.
바로 끝나는 시간으로 오름차순을 하면 같은 끝나는 시간 끼리 시작시간으로 정렬이 되지 않아 놓치는 부분이 생길 수 있다

그리고 정렬 순서도 바꿔서는 안된다.(시작시간 오름차순으로 마지막에 하면 끝나는 시간을 제대로 따질 수 없음)

입력 예시)
8
0 10
3 4
2 3
3 3
4 4
1 1
1 3
1 2

예시 출력)
1. 바로 끝나는 시간으로 오름차순
[[1, 1], [1, 2], [2, 3], [3, 3], [1, 3], [3, 4], [4, 4], [0, 10]]

2. 시작시간 오름차순 후, 끝나는 시간 오름차순
[[0, 10], [1, 1], [1, 2], [1, 3], [2, 3], [3, 3], [3, 4], [4, 4]]
[[1, 1], [1, 2], [1, 3], [2, 3], [3, 3], [3, 4], [4, 4], [0, 10]]



파이썬에서 여러 조건으로 정렬하는 방법(key에 튜플로 여러 인자를 주면 해당 안자의 순서대로 정렬)
->meeting_list = sorted(meeting_list, key = lambda x:(x[1], x[0]))

참고 : https://suri78.tistory.com/26

"""
