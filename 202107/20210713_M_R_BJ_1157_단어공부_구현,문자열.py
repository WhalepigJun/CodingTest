# BJ_1157_단어공부_구현,문자열
# https://www.acmicpc.net/problem/1157
# 시간 : 30분
# 
# 문자열을 중복없는 집합(set)으로 만들어주는 과정은 찾아보았음 


input_upper = input().upper() # 대문자로 만들어주고
set_input_upper = set(input_upper) # 중복을 뺀 집합을 이용
alpha = "" # 빈도가 가장 많은 알파벳
count = 0 # 빈도가 높은 알파벳을 찾기 위해 빈도를 저장할 변수
same = 0 # 빈도가 같은 알파벳이 있으면 1, 없으면 0
for i in set_input_upper: # 집합의 요소들로 반복문을 실행
    temp = input_upper.count(i) # 문자열에서 집합의 한 요소가 몇번들어가 있는지 확인하고 count에 저장
    if count<temp: # 현재 단어의 빈도가 더 크다면
        count = temp
        alpha = i
        same = 0
    elif count>temp: # 현재 단어의 빈도가 작으면
        continue
    elif count==temp: # 같으면 같다는 표시를 해줌
        same = 1
        
if same == 1:
    print("?")
else :
    print(alpha)


    
