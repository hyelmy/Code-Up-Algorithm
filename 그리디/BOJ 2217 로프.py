n = int(input())
rope = []

for i in range(n):
    rope.append(int(input()))

rope.sort(reverse = True)


answer = 0

for i in range(n):
    rope[i] = rope[i]*(i+1)


print(max(rope))

"""
나는 리스트 슬라이싱으로도 풀어보고,
하나씩 값을 새로운 리스트에 입력받아서 해당 리스트에서 제일 큰값을 갱신하는 방법으로도 풀어보았다.
씨나 자바에서는 될지 몰라도 파이썬에서는 시간 초과가 떴다...

생각해보니 반복문으로 리스트에 개수값만큼 곱해주고 제일 큰 값을 출력하면 되는 것이었다...

파이썬으로 풀려면 생각의 전환이 필요한 것 같다...!!!!!



n = int(input())
rope = []

for i in range(n):
    rope.append(int(input()))

rope.sort(reverse = True)

list= []

answer = 0
temp = 0
for i in range(n):
    temp += 1
    list.append(rope.pop(0))
    answer = max(answer, min(list)*temp)


print(answer)
    

            
n = int(input())
rope = []

for i in range(n):
    rope.append(int(input()))

rope.sort(reverse = True)

temp = 1
answer = rope[0]*temp

for i in range(len(rope)-1):
    temp += 1
    sum = min(rope[0:i+2])*temp
    if answer < sum:
        answer = sum

print(answer)

"""
