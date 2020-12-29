
num = int(input())


for i in range(num):
    n, m = list(map(int, input().split()))
    imp = list(map(int, input().split()))

    target = [1 if i==m else 0 for i in range(n)]
    count = 0

    while(True):
        
        if imp[0]  == max(imp):
            count +=1
            if target[0] == 1:
                print(count)
                break
            else:
                del imp[0]
                del target[0]
        else:
            imp.append(imp[0])
            del imp[0]
            target.append(target[0])
            del target[0]
            
    







"""
처음에 입력 부분이 이해가 잘 되지 않아서 엄청 힘들었다...
이해 되니까 쉽다!!

예제 설명 n = 문서개수, m = 몇 번째로 인쇄되는지 궁금한 문서가 있는 큐 위치

3 -> 3번 테스트 할거임
1 0 -> 첫번째 테스트 -> 문서 총 1개, 큐 인덱스로 0번째에 있는 문서가 몇번째로 인쇄되는지 궁금함
5 -> 현재 큐 중요도 순서

4 2 -> 두번째 테스트 -> 문서 총 4개, 큐 인덱스로 2번째에 있는 문서가 몇번째로 인쇄되는지 궁금함
1 2 3 4 -> 현재 큐 중요도 순서 

6 0 -> 세번째 테스트 -> 문서 총 6개, 큐 인덱스로 0번째에 있는 문서가 몇번째로 인쇄되는지 궁금함
1 1 9 1 1 1 -> 현재 큐 중요도 순서

"""
