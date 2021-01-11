# Code-Up-Algorithm 파이썬으로 도전하는 알고리즘 코딩테스트 준비

코딩테스트 준비를 위한 파이썬 문제 풀이를 올려놓는 레포지토리 입니다!
알고리즘 카테고리별로 분류하였고, 
문제이름이나 백준 알고리즘 문제 번호를 검색하면 
해당 문제의 풀이를 볼 수 있습니다!


코딩 테스트 보시는 분들 다들 화이팅!!


## 파이썬 문제 풀 때 꿀팁!

### 1. 코드업 100문제를 풀어보며 정리해본 알쏭달쏭한 파이썬 문법!(a,b,...는 문자, n, m,...은 숫자 표현)

- **C언어 처럼 print("%d" %a)로 출력할 수 있다.**

    - 많은 수 를 입력하고 싶을 땐 print("%d %d %d" %(a,b,c)) 이렇게 묶어서 표현할 수 있다!

- **print(a,b,c,sep=', ') 로 분별자를 넣을 수 있다!**

- **zfill()함수를 이용하여 자릿수를 맞출 수 있다!(날짜입력할 때 편리)**

- **파이썬으로 진수변환!**


    - %o 8진수

    - %x 16진수 소문자

    - %X 16진수 대문자

    - bin(n) 10진수 -> 2진수 변환 함수

    - oct(n) 10진수 -> 8진수 변환 함수

    - hex(n) 10진수 -> 16진수 변환 함수

    - int(n,8 or 16) 8,16진수인 a를 10진수로 변환 

- **문자 아스키 코드 변환!**


    - ord(a) 문자의 아스키 코드 값 돌려주는 함수

    - chr(n) 아스키코드를 문자로 변환

- **연산 관련**


    - sum(n,m,..) 합 구하는 내장 함수

    - round(n,m) n을 m자리까지 나오게끔 반올림

    - a<<b a에 2**b 만큼 곱함

    - not(a) -> true, false

    - int(not(a))->1, 0


- **한 줄로 조건문 쓰기(':'를 쓰지 않는다)**


    - ex)print(1) if a!=b else print(0)

- **파이썬에는 switch/case문이 없다!**


    - 사전형으로 충분히 간결하게 쓸 수 있기 때문! 사전형을 통해 key, value 값을 이용해보자

- **입력 받는 다양한 방법**


    - 개수입력받고 그다음 입력 리스트로 받음

```
n = int(input())

data = list(map(int, input().split()))
for i in data:
    print(i)
```
```
n, k = map(int, input().split())
money = []
for i in range(n):
    money.append(int(input()))
```
```
num = int(input())
time = []

for i in range(num):
    fir, sec = map(int, input().split())
    time.append([fir,sec])
```
```
#파이썬은 함수형 언어이다.
import sys
input = sys.stdin.readline
a,b = map(int,input().split())
```
```
#for문 돌려가면서 안받아도 되는 방법
map_list = [list(map(int, list(input()))) for _ in range(N)]

```

- **파이썬은 do/while문이 없음**

- **리스트 관련**


    - list.reverse() 리스트 거꾸로

    - list.count() 내가 찾고자 하는 값이 리스트에 몇개나 들어있는지 확인하고자 할 때
    
    - 리스트 슬라이싱
         - 양수: 연속적인 객체들의 제일 앞에서부터 0을 시작으로 번호를 매깁니다.

         - 음수: 연속적인 객체들의 제일 뒤에서부터 -1을 시작으로 번호를 매깁니다.

         - **list[a:b] -> a~b-1 범위

    - 정렬 방법
         - 파이썬에서 여러 조건으로 정렬하는 방법(key에 튜플로 여러 인자를 주면 해당 안자의 순서대로 정렬)
```
meeting_list = sorted(meeting_list, key = lambda x:(x[1], x[0]))
```

```c = sorted(a, key = lambda x : x[0])```
   
```
파이썬에서 여러 조건으로 정렬하는 방법(key에 튜플로 여러 인자를 주면 해당 안자의 순서대로 정렬)
list = sorted(list, key = lambda x:(x[1], x[0]))
```

- **1,0 반전 방법**
    - A[i][j] = 1 - A[i][j] (1에서 빼주면 된다!(값이 0 or 1일 경우에만)) 


