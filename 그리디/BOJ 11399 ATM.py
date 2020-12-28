num = int(input())
time = list(map(int, input().split()))
answer = 0

time.sort()

answer += time[0]

for i in range(len(time)-1):
    time[i+1] += time[i]
    answer +=time[i+1]


print(answer)

"""
인출하는데 걸리는 시간 리스트로 받아서 오름차순으로 정렬
time을 누적하며 더해야하기 때문에
time[i]의 값과 time[i+1]를 더한 값을 time[i+1]으로 저장하며 반복 계산
"""
