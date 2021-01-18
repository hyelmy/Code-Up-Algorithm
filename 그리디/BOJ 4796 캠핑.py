i =1
while(True):
    l, p, v = map(int,input().split())  #연속하는 P일 중, L일동안만 사용할 수 있다.
                                        #강산이는 이제 막 V일짜리 휴가를 시작했다

    if l == 0 and p == 0 and v == 0:    #l+p+v = 0으로 대체 가능
        break
    else:
        if v%p>l:
            print("Case "+str(i)+": "+str(v//p*l + l))

        else:
            print("Case "+str(i)+": "+str(v//p*l + v%p))
        i+=1

"""
나머지값이 l보다 커질 수 있다는 것에 조심해야함!
앞으로는 쓰기 쉽게
print("%d %d" %(a, b))
를 사용하
"""
