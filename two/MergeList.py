#coding:utf-8
#2.2算法
def MergeList(L1,L2):
    i = 0
    j = 0
    L = []
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            L.append(L1[i])
            i = i +1
        else:
            L.append(L2[j])
            j = j+1
    while i < len(L1):
        L.append(L1[i])
        i = i +1
    while j < len(L2):
        L.append(L2[j])
        j = j +1
    return L
 
L1 = [1,4,6,8]
L2 = [2,4,7,9,20]
print(MergeList(L1,L2))

        






