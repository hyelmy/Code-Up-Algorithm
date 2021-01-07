import sys
input = sys.stdin.readline

n = int(input())

temp = []


for _ in range(n):
    temp.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            temp[i][j]= temp[i][j] + temp[i-1][j]
            
            
        elif j == i:
            temp[i][j] = temp[i][j] + temp[i-1][j-1]

        else:
            temp[i][j] = temp[i][j] + max(temp[i-1][j-1], temp[i-1][j])
    
print(max(temp[-1]))

"""
DP는 진짜 말 그대로 구현해내면 되는 것 같다.
처음엔 위에서부터 하나하나 구해서 리스트에 담으려고 했지만
인덱스를 어떻게해야할지 감이 안잡혔다.

맨끝 값은 맨끝값만 더하면 되니까 양 끝의 경우를 따로 빼고
나머지값들은 양 옆의 요소들과 대각선이 서로 겹친다
이럴 경우 겹치는 값 중 최댓값을 구해서 더하면 구할 수 있는 최댓값이 된다.

"""
