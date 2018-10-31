#coding:utf-8
#简单选择排序
#每次找到最小值放在最前即可
def SelectionSort(L):
    for i in range(0,len(L)):
        temp = i
        for j in range(i+1,len(L)):
            #比较最小值，保留最小值得位置
            if L[temp] > L[j]:
                temp = j
        #最终，将最小值与第一个值得位置进行替换
        L[i],L[temp] = L[temp],L[i]
    return L

L = [9,8,7,6,5,4,3,2,1,0]
print(SelectionSort(L))






