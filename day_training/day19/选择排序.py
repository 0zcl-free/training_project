
import random





def select_sort(array):
    for i in range(len(array)-1):  # 找出最小的数放与array[i]交换
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp


if __name__ == "__main__":
    array = [265, 494, 302, 160, 370, 219, 247, 287,
             354, 405, 469, 82, 345, 319, 83, 258, 497, 423, 291, 304]
    print(array)
    select_sort(array)
    print(array)