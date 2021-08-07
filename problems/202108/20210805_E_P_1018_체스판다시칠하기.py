# BJ_1018_채스판 다시 칠하기 [브루트포스 알고리즘]
# https://www.acmicpc.net/problem/1018
# 시간 : 20분
# 처음에 문제 이해를 정확히 하지 못했음.

def find(hboard,x,y):
    count1=0
    for i in range(8):
        for j in range(8):
            if i in [0,2,4,6]:
                if j in [0,2,4,6]:
                    if hboard[i+x][j+y]=="B":
                        count1+=1
                else:
                    if hboard[i+x][j+y]=="W":
                        count1+=1
            else:
                if j in [0,2,4,6]:
                    if hboard[i+x][j+y]=="W":
                        count1+=1
                else:
                    if hboard[i+x][j+y]=="B":
                        count1+=1
    count2=0
    for i in range(8):
        for j in range(8):
            if i in [0,2,4,6]:
                if j in [0,2,4,6]:
                    if hboard[i+x][j+y]=="W":
                        count2+=1
                else:
                    if hboard[i+x][j+y]=="B":
                        count2+=1
            else:
                if j in [0,2,4,6]:
                    if hboard[i+x][j+y]=="B":
                        count2+=1
                else:
                    if hboard[i+x][j+y]=="W":
                        count2+=1
    
    cnt= count1 if count1<count2 else count2
    return cnt

n,m=map(int,input().split())
board=[list(input()) for i in range(n)]
min=64
for i in range(n-7):
    for j in range(m-7):
        tmp=find(board,i,j)
        if tmp<min:
            min=tmp
print(min)
