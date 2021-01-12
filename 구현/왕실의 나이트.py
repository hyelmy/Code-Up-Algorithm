loc = input()
loc_row = int(loc[1])  #숫자(행)
loc_col = ord(loc[0])-ord('a')+1 #알파벳(열)


steps = [(-2,1), (-2, -1), (2,-1), (2,1), (1,2),(1,-2), (-1,2), (-1,-2)]


cnt = 0
for step in steps:
    next_row = loc_row + step[0]
    next_col = loc_col + step[1]

    if next_row >=1 and next_row<=8 and next_col >= 1 and next_row <=8:
       cnt+=1

print(cnt)



"""
문제를 잘 못 이해했었다.
나이트가 이동할 수 있는 경우의 수가 계속 이동하면서 구해야되는 줄 알았는데

8가지 방향 중에 어떤 방향이 가능한지 count하는 것이었다.

만약에 내 생각대로 된 문제였으면 약간의 규칙같은게 더 있어야 될 것 같다.
"""
