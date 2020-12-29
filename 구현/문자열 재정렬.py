def solution(s):
    answer = len(s)

    for step in range(1, len(s)//2+1)
        compressed = ""
        prev = s[0, step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count+=1

            else:
                compressed += str(count) + prev if count>=2 else prev
                prev = s[j:j+step]
                count = 1

        compressed += str(count) + prev if count >=2 else prev
        answer = min(answer, len(compressed))

    return answer
    
                
"""
어떻게 풀지는 알았는데
막상 구현해내려고 하니 머리가 아팠다....

슬라이스를 했는데 step을 계속 높이는 과정이 좀 어려웠다..
다음에 봤을 땐 쉬운문제라고 생각할만큼 연습해보자!

"""
