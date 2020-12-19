n = map(int, input().split())

data = list(map(int, input().split()))
data.sort(reverse=True)

i=0
answer = 0

while(True):
    if i < len(data):
        i += data[i]
        answer +=1

    else:
        break

print(answer)
