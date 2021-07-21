# BJ_1966_프린터 큐 [큐]
# https://www.acmicpc.net/problem/1966
# 시간 : 측정 불가
# 리뷰 : 큐에 대한 복습은 금방 감을 잡았음. 이 문제에서 중요하지 않은 문서를 큐 뒤로 넘기는 과정에서 우리가 원하는 문서의 위치를 다시 지정해주는 조건에 대해서 시간이 걸림.
# 다시 풀어보는것이 좋음.


import sys
testcases = int(sys.stdin.readline())
n=[]
m=[]
important=[]
for testcase in range(testcases):
    tmp_n, tmp_m = map(int, sys.stdin.readline().split())
    n.append(tmp_n)
    m.append(tmp_m)
    important.append(map(int, sys.stdin.readline().split()))

class Queue:
    def __init__(self):
        self.item=[]
        self.f=0
        self.r=0
    def push(self, value):
        self.item.append(value)
        self.r+=1
        return
    def pop(self):
        if self.f==self.r: # 큐가 비어있을 때
            return False
        else:
            result=self.item[self.f]
            self.f+=1
            return result
    def isinMoreImportant(self): # 더 중요한 문서가 있을 때
        if len(self.item[self.f:])==1: # 큐에 요소가 하나만 존재
            return False
        now = self.item[self.f]
        important = max(self.item[self.f+1:])
        if now<important:
            return True
        else:
            return False
    def return_f(self): # 현재 위치
        return self.f
    def return_r(self): # 현재 위치
        return self.r
    def return_item(self):
        return self.item
    
for testcase in range(testcases):
    que = Queue()
    for i in important[testcase]: # 입력받은 문서의 중요도를 큐에 넣음
        que.push(i)
    cnt=0 # 출력 번호
    pd=m[testcase] # 원하는 문서의 위치
    while True: # 원하는 문서가 출력되면 종료(break)
        if que.isinMoreImportant(): # 더 중요한 문서가 있으면
            if que.return_f()==pd: # 뒤로 보내는 문서가 원하는 문서이면 그 위치를 다시 저장
                pd=que.return_r()
            que.push(que.pop())
        else : # 제일 중요한 문서일때
            if que.return_f()==pd:
                cnt+=1
                print(cnt)
                break
            que.pop()
            cnt+=1
