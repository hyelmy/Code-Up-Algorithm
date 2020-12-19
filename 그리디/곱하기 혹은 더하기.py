import sys

input = sys.stdin.readline().rstrip()

a = list(map(int, input))

answer = 0

for i in a:
    if i <= 1 or answer==0 :
        answer += i
    else:
        answer *= i

print(answer)
