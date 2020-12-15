import sys


input = sys.stdin.readline().rstrip()

a = list(map(int, input))

count0 = 0
count1 = 0

if a[0] == 1:
    count0 += 1
else:
    count1 += 1


for i in range(len(a)-1):
    if a[i] != a[i+1]:
        if a[i+1] == 1:
            count0 +=1
        else:
            count1 +=1
    else:
        continue

print(min(count0, count1))


"""
이 문제는 첫단추를 잘 꿰매는게 중요한 문제였던 것 같다.

a[0]을 확인했으니 그 다음부터 보면 되겠지하고 range(1, len(a)-1)로 해서
첫번째요소와 두번째 요소와 비교를 하지 못해서 자꾸 오류가 났당....ㅠㅜ 

실수 그만!!!
"""
