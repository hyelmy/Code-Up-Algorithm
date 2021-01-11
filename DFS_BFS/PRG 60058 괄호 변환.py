
#균형잡힌 괄호 문자열 u,v 나누기
def make_u(li):
    count_l = 0
    count_r= 0
    for i in range(len(li)):
        if li[i] == '(': 
            count_l += 1
        else:
            count_r += 1

        if count_l == count_r:  #첫번째로 '(',')'갯수가 같은 위치 찾기
            break
    u = li[:i+1]
    v = li[i+1:]

    return u, v


#u가 올바른 괄호 문자열 여부 확인하기
def check_u(u):
    stack = []
    for i in range(len(u)):
        if u[i] =='(':
            stack.append('(')

        else:
            if not stack:   #스택 확인하는 도중에 스택이 비워짐 -> '(' ')'순서가 맞지 않음 -> 올바른 괄호 문자열 x
                return False
            stack.pop()
    return True 



def solution(w):
    if not w:
        return "" #1. 입력이 빈 문자열인 경우
    
    u, v = make_u(w) #2. u,v 분리하여 리스트 생성
    
    if check_u(u):  #3. u가 올바른 괄호 문자열인지 확인, 수행한 결과 문자열을 u에 이어 붙인 후 반환 후 재귀
        return ''.join(u)+solution(v)
    
    else:   #4. u가 올바른 괄호 문자열이 아닌 경우
        answer = '('    #4-1. 빈 문자열에 첫번째 문제로 '('를 붙임
        answer += solution(v)   #4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙임
        answer += ')'   #4-3. ')'를 다시 붙인다

        for i in u[1:-1]: #4-4. u의 첫번째, 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향 뒤집어서 뒤에 붙인다
            if i =='(':
                answer += ')'
            else:
                answer +='('

        return answer   #4-5생성된 문자열 반환

"""
solution함수 짜는 게 좀 막막했다
문제 설명이 상세해서 그대로 짰으면 됐는데, 아직 재귀에 대해 이해를 완벽히 못했나보다ㅠ

근데 저 함수 나누는건 맞게 잘했다!!
점점 발전 하는 모습 좋아 더 열심히 하자!!!

"""
