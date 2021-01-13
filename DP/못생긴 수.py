n = int(input())

answer= [0]*n
answer[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2,3,5


for i in range(1, n):
    
    #가능한 곱셈 결과 중에서 가장 작은 수를 선택
    answer[i] = min(next2, next3, next5)

    
    if answer[i] == next2:
        i2 += 1
        next2 = answer[i2]*2
        print("i2 = "+str(next2))
    if answer[i] == next3:
        i3 +=1
        next3 = answer[i3]*3
        print("i3 = "+str(next3))

    if answer[i] == next5:
        i5 += 1
        next5 = answer[i5]*5
        print("i5 = "+str(next5))

print(answer[n-1])


        
"""
못생긴 수에 2,3,5를 곱한 수 또한 못생긴 수!!!
이걸 빨리 파악했어야했다,,,

i2,i3,i5값을 변화시키면서 작은 수 부터 차례대로 못생긴 수를 구하면 된다

자세한 풀이는
https://hyelmy.github.io

"""
