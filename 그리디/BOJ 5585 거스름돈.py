cost = int(input())
cost = 1000 - cost
list = [500, 100, 50, 10, 5, 1]
answer = 0


i = 0    
while(cost):

    answer += cost//list[i]
    cost %= list[i]
    
    if cost == 0:
        break
    i +=1


print(answer)
