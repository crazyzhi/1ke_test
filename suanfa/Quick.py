#coding:utf-8
#快速排序算法
##核心：以数组头为基准，从两端开始进行比较，从先尾部开始
#从尾巴开始找到第一个比基准值小的值时停下，在从头开始找到比基准值大的值停下，两个值进行交换
#交换完之后，尾部的继续向前查找，首部也继续向前查找，都停下时，交换之
#当首部的索引值与尾部的索引值相等时，停止查找，将基准值于现在索引的位置值与之交换
#此时，在基准值前 的值都比基准值小，在基准值后的值都比基准值大
#现在，以基准值为分割，前的堪称一个新数组，后的堪称一个新数组，重复最开始时时的查找
def QuickSort(L,low,high):
    i = low
    j = high
    if i > j:
        return L
    temp = L[low]
    while i != j:
        #找到比基准值小的值，然后停
        while L[j] >= temp and i < j:
            j = j -1
        #找到比基准值打的值，然后停
        while L[i] <= temp and i < j:
            i = i +1
        #如果i的值小于j，将两个值进行调换
        if i < j:
            nu = L[i]
            L[i] = L[j]
            L[j] = nu
    #因为最后停下来是因为i = j 所以讲索引为i的值与基准值进行调换
    #此时，在基准值两侧的数值，左边都比它小，右边都比它大

    mu = L[i]
    L[i] = temp
    L[low] = mu
    #重复上面的操作，只不过low和high的值都有了变化，但原始的L内容还是不变的
    QuickSort(L,low,i-1)
    QuickSort(L,i+1,high)
    return L


if __name__ == "__main__":
    L = [14,5,18,1,45,3,9,6,23]
    low = 0
    high = len(L) - 1
    print(QuickSort(L,low,high))

