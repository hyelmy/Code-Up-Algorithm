#1번째 풀이

m, n = map(int, input().split())

data = list(map(int, input().split()))

answer = 0

for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] == data[j]:
            continue
        
        else:
            answer +=1

print(answer)


#2번째 풀이

m, n = map(int, input().split())

data = list(map(int, input().split()))

array = [0]*11

for x in data:
    array[x]+=1


result = 0

for i in range(1, m+1):
    m -= array[i]
    result += m * array[i]

print(result)



"""
처음엔 정말 효율적이지 못한 방법으로 풀었다.
조합의 개념을 써야된다는 것은 알았지만 조합을 하나하나씩 구해가며 푸는 방법이었다.


난 언제쯤 알고리즘 문제를 잘 풀 수 있을까...8ㅁ8
그리디 개념이 쉽긴한데 막상 적용하기 너무 어려운 것 같다....

더 노력해야겠다!




"""
