#coding:utf-8
#合并两个列表算法

def union(L1,L2):
    L3 = L1
    for i in L2:
        if i not in L1:
            L3.append(i)
    return L3

L1 = [1,2,3]
L2 = [3,5,6]

print(union(L1,L2))





