point = list(map(int,input()))

sum1=0
sum2 = 0
for i in range(int(len(point)/2)):
    sum1 += point[i]
    sum2 += point[-(i+1)]

if sum1==sum2:
    print("LUCKY")

else:
    print("READY")

"""
/, //, % 나누기 연산은 모두 결과가 float으로 나온다
하지만 range()에선 int형만 가능하므로
int()로 바꿔줘야한다.


"""
    
