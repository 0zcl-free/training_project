

def quick_sort(array, left, right):
    '''
    :param array:
    :param left: 列表的第一个索引
    :param right: 列表最后一个元素的索引
    :return:
    '''
    if left >= right:
        return

    low = left
    high = right
    key = array[low]  # 第一个值，即基准元素

    while low < high:  # 只要左右未遇见
        while low < high and array[high] > key:  # 找到列表右边比key大的值 为止
            high -= 1
        # 此时直接 把key跟 比它大的array[high]进行交换
        array[low] = array[high]
        array[high] = key

        while low < high and array[low] <= key:  # 找到key左边比key大的值，这里为何是<=而不是<呢？你要思考。。。
            low += 1
        # 找到了左边比k大的值 ,把array[high](此时应该刚存成了key) 跟这个比key大的array[low]进行调换
        array[high] = array[low]
        array[low] = key

    quick_sort(array, left, low-1)  # 最后用同样的方式对分出来的左边的小组进行同上的做法
    quick_sort(array,low+1, right)  # 用同样的方式对分出来的右边的小组进行同上的做法


if __name__ == '__main__':
    array = [8,4,1, 14, 6, 2, 3, 9,5, 13, 7,1, 8,10, 12]
    print("-------排序前-------")
    print(array)
    quick_sort(array, 0, len(array)-1)
    print("-------排序后-------")
    print(array)