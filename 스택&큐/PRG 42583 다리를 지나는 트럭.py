from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque([0]*bridge_length)
    total_weight = 0
    while(True):
        if not truck_weights:
            answer += bridge_length
            break
        v = q.popleft()
        total_weight -= v
        if total_weight+truck_weights[0] <= weight:
            q.append(truck_weights[0])
            total_weight += truck_weights[0]
            del truck_weights[0]
        else:
            q.append(0)
        print(q)
        answer +=1
    print(answer)
    return answer
    
solution(100, 100, [10,10,10,10,10,10,10,10,10,10])

"""
큐를 어떻게든 해보려다 안돼서 질문하기 버튼을 눌러서 보는데 어떤 친절하신 분이 
'큐를 쓰는 것까지는 알겠는데 활용하는 방법이 도저히 생각나지 않는 분들을 위해'라는 제목으로 글을 올리셨길래 보게되었다.
---
큐는 선입선출의 구조임을 이용해
시간에 따라 한칸씩 이동하는 것을 구현한다면

for(int i=0;i<bridge_length;i++)
    q.push(0);
이렇게 해서 큐를 다리라고 생각하고 공기(0)들을 미리 채운 다음에
매 시간마다 pop하고 현재 다리 위의 무게에 따라 트럭을 push하거나 공기(0)를 push해보는건 어떨까요!
---
라는 조언을 해주셨는데 이를 이용해서 풀어보았는데 큐에 들어갈때마다 truck_weight요소를 지웠더니 
처음엔 큐에 들어갈때마다 마지막 truck_weights 요소가 들어가자마자 끊겼다.ㅜㅜㅠ

저 마지막 요소를 어떻게 해야하나 고민해보다가
어차피 마지막 요소가 들어가면 무게는 맞춰져있는 상태이고 마지막 요소는 길이만큼 들어가면 되기 때문에
마지막 요소가 들어갈 경우 answer += bridge_length를 해주었더니 통과되었다!!
이게 괜찮은 건진 모르겠지만 간만에 통과한 문제였다...ㅠㅠ 이제 더 열심히 하자
"""
