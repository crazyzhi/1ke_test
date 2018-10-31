#coding:utf-8
import math
#希尔排序
def ShellSort(L):
    n = len(L)
    #向上取整，为最初的分组数量
    gap = math.ceil(n/2)
    #当gap值为1时，算法进行最后一次排序，相邻的元素都会进行一次排序
    while gap > 0:
    
        for i in range(gap,len(L)):
            j = i
            #将分组数看成尾，用尾和头进行对比
            while j - gap >= 0 and L[j] < L[j-gap]:
                L[j],L[j-gap] = L[j-gap],L[j]
                j = gap -1
        #gap等于1时，进行了最后一次排序，排序完成后，让gap=0，结束循环
        if gap == 1:
            gap = 0
        gap = math.ceil(gap/2)
        
    return L
La = [9,8,7,6,5,4,3,2,1,0]
print(ShellSort(La))




