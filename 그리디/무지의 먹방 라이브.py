#food_times = list(map(int, input().split()))

#k = int(input())

def solution(food_times, k):
    food_list = [] 
    totalTime = 0

    #[[음식의 번호, 음식 먹는 시간],...]
    for i in range(0, len(food_times)):
        food_list.append([i, food_times[i]])
        totalTime += food_times[i]
        
    #음식의 양보다 k가 크면 더 섭취할 음식이 없으므로 -1 반환
    if totalTime  <= k:
        return -1

    #음식의 양이 작은 것 먼저 사라지기 때문에 음식의 양에 따라 정렬
    food_list.sort(key = lambda x:x[1])

    #음식을 다먹기까지 없어지는 시간 = 음식의 양 * 한바퀴 돌 때 걸리는 시간(음식의 개수)
    delTime = food_list[0][1]*len(food_list)
    i = 1

    #delTime<k이면 음식을 다 먹고도 시간이 남음(즉, 다 먹고 그 다음 음식의 양이 적은 음식을 판단해야함)
    while delTime < k:

        #다 먹기 가능하다고 판단하여 k시간에서 음식을 다 먹는데 걸리는 시간을 뺌
        k -= delTime

        #(현재의 음식시간 - 이전 음식의 시간) * 현재 남은 음식 개수
        #현재의 음식시간 - 이전 음식의 시간하는 이유: 현재 음식시간(현재까지  누적)- 이전 음식시간(이미 이전에 먹었던 음식)
        #(5-2)*4 = 5*4-2*4
        delTime = (food_list[i][1] - food_list[i-1][1])*(len(food_list)-i)

        #음식이 다먹고 사라지니 음식을 제거함
        i += 1

    #delTime>=k이면 k초 넘어서까지 음식을 먹었다는 뜻
    #그때 stop! 남은 음식부터 번호 순으로 정렬 후 k값에 해당되는 음식 번호 찾기
    food_list = sorted(food_list[i-1:], key=lambda x: x[0])
    return food_list[k%len(food_list)][0]+1

print(solution([6,5,2,2,7], 13))

"""
책에서 나오는 우선순위 큐를 이용한 방법
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_value = 0
    previous = 0
    length = len(food_times)
    
    while sum_value +((q[0][0] - previous)*length)<=k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous)*length
        length -= 1
        previous = now
        
    result = sorted(q, key= lambda x:x[1])
    return result[(k-sum_value)%length][1]


    와 진짜 이런 생각을 하는 사람은 도대체,,,,
    처음엔 하나씩 돌리면서 풀었었다. 이 방법은 효율성 테스트에서 통과하지 못한다고 한다.
    난 아직 멀었다...ㅠㅜㅠㅜㅠ
"""

