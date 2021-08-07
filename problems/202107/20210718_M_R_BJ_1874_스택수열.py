# BJ_1874_스택 수열_[스택]
# https://www.acmicpc.net/problem/1874
# 시간 30분
# 오랜만에 스택을 이용해서 문제를 풀었다. 처음에는 조금 막막했는데 금방 느낌을 찾았다.
# 문제는 전역변수 설정 함수 밖에서 변수를 정의해줬는데 이게 함수 안에서 할당할때는 UnboundLocalError를 발생시켰다.
# 찾아보니까 함수 안에서도 global 변수라고 선언해주어야했다. 이 부분에 대해서만 검색했다.


stack = [0 for i in range(1000000)] # n이 1000000까지 가능하므로
top = -1
result=[]

def push(k):
    global stack
    global top
    global result
    top+=1
    stack[top]=k
    result.append("+")
    
def pop():
    global top
    global result  
    top-=1
    result.append("-")

def check(): # 스택의 top 위치의 값 리턴
    return stack[top]

import sys
n=int(sys.stdin.readline())
sq=[]
for i in range(n):
    sq.append(int(sys.stdin.readline()))

num = 1 # 1부터 n까지의 수를 스택에 넣는다.
pos = 0 # sq의 위치에 대한 변수
while True:
    if pos==n:
        for r in result:
            print(r)
        break
    i = sq[pos]
    if top==-1: # 스택에 아무것도 없으면
        push(num) # push
        num+=1
    if check()==i: # 스택의 top 위치의 값과 만들어야하는 수열 값과 같으면
        pop()
        pos+=1 # 다음 위치로
        continue
    else : # 다르면
        push(num)
        num+=1
    if num==n+2:
        print("NO")
        break
        
