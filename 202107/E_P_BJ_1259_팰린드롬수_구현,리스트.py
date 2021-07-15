# BJ_1259_팰린드롬수_구현,리스트
# https://www.acmicpc.net/problem/1259
# 15분
# 알고리즘은 금방했는데, 입력하는 문제에서 조금 시간걸렸음. input()의 입력은  문자열로 들어온다. 

data = []
while True: # 데이터 입력받아서 data list에 추가
    i = input().strip()
    if i=="0":
        break
    else:
        data.append(i)

output = []
for i in range(len(data)):
    stin = str(data[i])
    tmp="yes"
    for st in range(int(len(stin)/2)):
        if stin[st] == stin[len(stin)-1-st]: # 대칭인지 확인
            continue
        else: # 대칭이 아니라면
            tmp="no"
    output.append(tmp)

for o in output:
    print(o)
     
