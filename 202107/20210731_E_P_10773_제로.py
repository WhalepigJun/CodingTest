# BJ_10773_제로 [구현, 자료구조, 문자열, 스택]
# https://www.acmicpc.net/problem/10773
# 시간 : 10분
# 리뷰 : 스택을 이용하는 문제.

import sys
k=int(sys.stdin.readline())
nums=[]
ps=0
for i in range(k):
    num=int(sys.stdin.readline())
    if num==0:
        ps-=1
    else :
        if len(nums)<=ps:
            nums.append(num)
            ps+=1
        else:
            nums[ps]=num
            ps+=1
print(sum(nums[:ps]))
