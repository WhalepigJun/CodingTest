# BJ_9012_괄호 [자료구조, 문자열, 스택]
# https://www.acmicpc.net/problem/9012
# 시간 : 20분
# 리뷰 : 스택이용


class Stack:
    def __init__(self):
        self.stack=[]
    def insert(self,value):
        self.stack.append(value)
    def pop(self):
        if len(self.stack)==0:
            return
        return self.stack.pop()
    def isEmpty(self):
        isempty = False
        if len(self.stack)==0:
            return True
        return isempty
    def check(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.stack[len(self.stack)-1]
        
def isVPS(brackets):
    stack = Stack()
    isvps = False
    for bracket in brackets:
        if bracket=="(":
            stack.insert(bracket)
        elif bracket==")":
            if stack.check()=="(":
                stack.pop()
            else:
                stack.insert(bracket)
    if stack.isEmpty():
        isvps=True
    return isvps

import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    if isVPS(input()):
        print("YES")
    else:
        print("NO")
