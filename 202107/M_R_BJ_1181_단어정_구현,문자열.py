# BJ_1181_단어정렬_구현,문자열
# https://www.acmicpc.net/problem/1181
# 시간 : 20분
# 문자열 정렬과정에서 다중조건을 이용하는 lambda 사용하는것은 찾아보았다.

c = int(input())
data =[]
for c in range(c):
    data.append(input())

s = set(data) # 집합으로 중복제거
l = list(s) # 리스트로 변경
l.sort(key=lambda x:(len(x), x))
for i in l:
    print(i)
