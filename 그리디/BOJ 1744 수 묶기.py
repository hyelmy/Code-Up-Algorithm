n = int(input())
negative = []
positive = []
temp = 0
for i in range(n):
    a = int(input())
    if a > 1:
        positive.append(a)

    elif a ==1:
        temp +=1
    else:
        negative.append(a)

negative.sort()
positive.sort(reverse= True)


for i in range(0, len(negative), 2):
    if i+1<len(negative):
        temp += negative[i]*negative[i+1]
    else:
        temp += negative[i]

for i in range(0, len(positive), 2):
    if i+1 < len(positive):
        temp += positive[i]*positive[i+1]

    else:
        temp += positive[i]
print(temp)


"""
** 0을 포함한 음수는 작은 수 부터 묶는다 & 1보다 큰 수는 큰 수부터 묶는다 & 숫자가 1인 경우 묶지 않는다(따로 빼주기) **

마이너스끼리 곱하면 +가 되는 것!!과 -1*0은 0이 되는 것을 처리하지 못했다
큐로 구분지어서 했었는데 불필요한 과정이었던 것 같다.
그리고 정렬을 했으면서 정렬한 보람 없게 한 것 같기도 하
for i in range(1, len(array)):
    print("%d번째 수 : %d" %(i, array[i]))
    if not dq:
        if array[i]>1:
            dq.append(array[i])
            print(dq)
        else:
            temp += array[i]
            print(temp)
    else:
        if array[i]>1:
            n = dq.popleft()
            print(dq)

            temp += n*array[i]
            print(temp)

        else:
            n = dq.popleft()
            print(dq)

            temp += n + array[i]
            print(temp)

print(temp)

"""
