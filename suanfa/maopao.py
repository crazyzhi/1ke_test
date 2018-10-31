#coding:utf-8
#冒泡排序，逻辑上很简单，就是进行比较，找到最小的与之交换位置
def mao(L):
    for i in range(0,len(L)):
        for j in range(i+1,len(L)):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L

L = [1,9,2,3,5,0,8]
print(mao(L))


