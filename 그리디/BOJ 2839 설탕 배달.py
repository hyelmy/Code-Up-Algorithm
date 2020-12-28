sugar = int(input())
answer = 0

while(sugar >=0):
    if sugar % 5 ==0:
        answer += sugar //5
        sugar %= 5
        print(answer)
        break
    sugar -= 3
    answer += 1
    
    if sugar < 0 :
        print(-1)
        break




"""
5로 나눠질 때까지 -3으로 쪼개나가는 방식이다.
음수이면 -3이 계속 이뤄지다가 3으로도 쪼갤 수 없는 경우이므로 -1 반환

"""
