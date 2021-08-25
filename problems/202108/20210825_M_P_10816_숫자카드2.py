import sys
input=sys.stdin.readline
N=int(input())
cards=list(map(int,input().split()))
M=int(input())
num_list=list(map(int,input().split()))

hash_dic={}
for n in cards:
    if n in hash_dic:
        hash_dic[n]+=1
    else:
        hash_dic[n]=1

for i in range(len(num_list)):
    if num_list[i] in hash_dic:
        print(hash_dic[num_list[i]], end=" ")
    else:
        print(0, end=" ")
