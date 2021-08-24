import sys
input = sys.stdin.readline
N = int(input())
li = []
for _ in range(N):
    li.append(list(input().split()))
li = sorted(li,key=lambda x : int(x[0]))

for i in range(N):
    print(li[i][0], li[i][1])
