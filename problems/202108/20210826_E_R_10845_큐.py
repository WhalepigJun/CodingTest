# BJ_10845_큐 [자료구조, 큐]
# https://www.acmicpc.net/problem/10845
# 시간 : 20분
# 리뷰 : 큐의 기본

class QUEUE:
    def __init__(self):
        self.queue=[]
        
    def push(self,value):
        self.queue.append(value)
    
    def pop(self):
        if self.empty():
            return -1
        else:
            result = self.queue[0]
            self.queue.pop(0)
            return result
    
    def size(self):
        return len(self.queue)
    
    def empty(self):
        result=0
        if len(self.queue)==0:
            result=1
        return result
    
    def front(self):
        if self.empty():
            return -1
        else:
            return self.queue[0]
        
    def back(self):
        if self.empty():
            return -1
        else:
            return self.queue[self.size()-1]

import sys
input=sys.stdin.readline
queue=QUEUE()
N=int(input())
for _ in range(N):
    command = input().rstrip()
    if 'push' in command:
        value = command.split()[1]
        queue.push(value)
    elif 'front'==command:
        print(queue.front())
    elif 'back'==command:
        print(queue.back())
    elif 'size'==command:
        print(queue.size())
    elif 'empty'==command:
        print(queue.empty())
    elif 'pop'==command:
        print(queue.pop())
