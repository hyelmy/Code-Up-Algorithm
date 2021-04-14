def solution(name):
    n = list(name)  #입력된 이름
    check = []
    for i in range(len(name)):  #체크 확인 리스트
        check.append(0)
        
    count = 0
    i = 0
    
    while(True):
        print(check)
        print("첫번째 카운트 :"+str(count))
        if 0 not in check:  #체크를 다 한 경우
            break
        else:
            if (n[i]=='A'):     #A를 만난경우 더 짧은 경우의 수 구해야함.
                if (check[i] == 0): #체크하지 않은 A인 경우 체크해줌
                    check[i] = 1
                for j in range(i, len(name)):   #앞으로 구하는 게 빠른지 뒤로가는 게 빠른지 경우의 수를 구해줌
                    if(n[j] != 'A' and check[j] ==0): #A가 아니고 체크하지 않은 경우
                       temp1 = j-i      #뒤로 가는 경우
                       temp2 = i+len(name)-j #앞으로 가는 경우
                       print(temp1)
                       print(temp2)
                       check[j] = 1
                       count += min(temp1, temp2)
                       print(count)
                       print("알파함수값시바"+ str(check_alpha(n[j])))
                       count += check_alpha(n[j])
                       i = j+1
                       print("a만났을 때 카운트 :"+str(count))

                       break

                    print("A 만남")

            elif(n[i] != 'A' and check[i]==0):      #A가 아니고 확인하지 않은 경우
                print(n[i])
                count += check_alpha(n[i])          #알파벳 순서 만큼 count++
                check[i] = 1                        #확인 표시
                i += 1
                if (i>len(name)-1):
                    print("a 아닐때 카운트 :"+str(count))
                    continue
                else:
                    count+=1
                    continue
          
            else:       #A가 아니고 확인한 경우 continue
                i += 1
                print("a 아니고 확인했을 경우 카운트 :"+str(count))
                continue

    return count            #최종 count 반환


def check_alpha(alpha1):
    num1 = ord(alpha1)-65
    temp1 = 1+ord('Z')-ord(alpha1)
    print(num1)
    print(temp1)
    return min(temp1, num1)
    

solution("JEROEN")
print()
solution("JAN")
