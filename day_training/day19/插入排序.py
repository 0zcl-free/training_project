
import time


def insertion_sort(array):
    for i in range(1, len(array)):  # 对第i个元素进行插入，i前面是已经排序好的元素
        position = i  # 要插入数的下标
        current_val = array[position]  # 把当前值存下来
        # 如果前一个数大于要插入数，则将前一个数往后移，比如5,8,12,7;要将7插入，先把7保存下来，比较12与7，将12往后移
        while position > 0 and current_val < array[position-1]:
            array[position] = array[position-1]
            position -= 1
        else:  # 当position为０或前一个数比待插入还小时
            array[position] = current_val




if __name__ == "__main__":
    array = [92, 77, 67, 8, 6, 84, 55, 85, 43, 67]
    print(array)
    time_start = time.time()
    insertion_sort(array)
    time_end = time.time()
    print("time: %s" % (time_end-time_start))
    print(array)