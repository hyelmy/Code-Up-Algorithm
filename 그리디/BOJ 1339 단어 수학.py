n = int(input())
array = []
for i in range(n):
    array.append(input())

alphabet = [0]*26
num = 9



for i in range(n): #단어 갯수 만큼
    k = len(array[i])
    for j in range(k): #문자 하나하나 돌기
        alphabet[ord(array[i][j])-65] += 10**(k-j-1)
alphabet.sort(reverse=True)

answer = 0
for i in alphabet:
    answer += num*i
    num -= 1
print(answer)

"""
처음엔 완전탐색으로 풀려고 했다가 큰 낭패를 보았다....

이 문제는 각 자리의 중요도를 기록하는 것이 중요했다!

ABA를 예시로 들면
A -> 100의 자리 + 1의 자리 = 100 +1 = 101
B -> 10의 자리 = 10

중요도를 기록하고 높은 순서대로 9~0을 차례대로 매기면 되는 문제였다!
처음에 아이디어를 떠올리는 게 중요한 것 같다...!


*** 'A'의 아스키코드 = 65 'a'의 아스키코드 = 97 알파벳은 26개
*** ord()는 문자의 아스키 코드 값을 돌려주는 함수이다.


"""
