# BJ_10828_스택 [자료구조, 스택]
# https://www.acmicpc.net/problem/10828
# 시간 : 20분
# 리뷰 : 스택의 기본, 인터넷에 공개되어있는 스택 다른 방법도 확인해보자.

import sys

class Stack:
    st=[]
    ps=0
  
    def push(self,value):
        if len(self.st)<=self.ps:
            self.st.append(value)
            self.ps+=1
        else:
            self.st[self.ps]=value
            self.ps+=1
    def pop(self):
        if self.ps==0:
            return -1
        self.ps-=1
        return self.st[self.ps]
    def size(self):
        return self.ps
    def empty(self):
        if self.ps==0:
            return 1
        else:
            return 0
    def top(self):
        if self.ps==0:
            return -1
        else:
            return self.st[self.ps-1]

stack=Stack()
n=int(sys.stdin.readline())
for i in range(n):
    command=sys.stdin.readline()
    if "push" in command:
        c,n=command.split()
        stack.push(int(n))
    elif "pop" in command:
        print(stack.pop())
    elif "size" in command:
        print(stack.size())
    elif "empty" in command:
        print(stack.empty())
    elif "top" in command:
        print(stack.top())