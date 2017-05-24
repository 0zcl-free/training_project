
def sift_down(arr, node, end):
    """
    调整成大顶堆
    :param arr: 列表
    :param node: 父结点，最后一个有子节点的孩子开始直到根结点
    :param end: 列表最后一个元素下标
    :return: 无
    """
    root = node
    # print(root,2*root+1,end)
    while True:
        # 从root开始对最大堆调整
        # 当列表第一个是以下标0开始，结点下标为i,左孩子则为2*i+1,右孩子下标则为2*i+2;
        # 若下标以1开始，左孩子则为2*i,右孩子则为2*i+１
        child = 2 * root + 1  # left child
        if child > end:
            # print('break',)
            break
        # print("v:", root, arr[root], child, arr[child])
        # print(arr)
        # 找出两个child中交大的一个
        if child + 1 <= end and arr[child] < arr[child + 1]:  # 如果左边小于右边
            child += 1  # 设置右边为大

        if arr[root] < arr[child]:
            # 最大堆小于较大的child, 交换顺序
            tmp = arr[root]
            arr[root] = arr[child]
            arr[child] = tmp

            # 正在调整的节点设置为root
            # print("less1:", arr[root],arr[child],root,child)

            root = child  # 交换之后以交换子结点为根的树可能不满足堆排序，需重新调整
            # [3, 4, 7, 8, 9, 11, 13, 15, 16, 21, 22, 29]
            # print("less2:", arr[root],arr[child],root,child)

        else:
            # 无需调整的时候, 退出
            break

    print('-------------node:', arr[root])
    print(arr)



def heap_sort(arr):
    # 从最后一个有子节点的孩子开始调整最大堆，注意: 第一个结点的下标为０(也有些博客是以1开始的)
    first = len(arr) // 2 - 1
    for i in range(first, -1, -1):  # 初始化大顶堆
        sift_down(arr, i, len(arr) - 1)

    print('--------end---', arr)

    # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]  # 将排好的大顶堆最大数放到堆的最后一个
        sift_down(arr, 0, end - 1)  # 重新排成大顶堆


if __name__ == "__main__":
    array = [16,7,3,20,17,8]
    print(array)
    heap_sort(array)
    print(array)