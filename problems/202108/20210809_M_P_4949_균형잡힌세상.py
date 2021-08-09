# BJ_4949_균형잡힌 세상 [자료 구조, 문자열, 스택]
# https://www.acmicpc.net/problem/4949
# 시간 : 30분
# 리뷰 : 스택 이용, 구현 방법은 바로 알았는데, 반복문을 통해 클래스를 새로 만들어주는 듯 했지만 실제로는 아니었음
# 초기화 메소드를 정의해서 반복문마다 실행해주어 해결

import sys
input=sys.stdin.readline
sentences=[]
while True:
    tmp=input().rstrip()
    if tmp==".":
        break
    sentences.append(tmp)
    
class Stack:
    st=[]
    def insert(self,value):
        self.st.append(value)
    def pop(self):
        if self.isEmpty():
            return
        else:
            result=self.st.pop()
            return result
    def check(self):
        if self.isEmpty():
            return "isEmpty"
        else:
            return self.st[-1]
    def isEmpty(self):
        if len(self.st)==0:
            return True
        else:
            return False
    def initial(self):
        self.st.clear()

for sentence in sentences:
    sentence=sentence.replace(" ","")
    stack=Stack()
    stack.initial()
    for i in sentence:
        if i in "([":
            stack.insert(i)
        elif i==")":
            if stack.isEmpty():
                stack.insert(i)
            elif stack.check()=="(":
                stack.pop()
            else:
                stack.insert(i)
        elif i=="]":
            if stack.isEmpty():
                stack.insert(i)
            elif stack.check()=="[":
                stack.pop()
            else:
                stack.insert(i)
    if stack.isEmpty():
        print("yes")
    else:
        print("no")
