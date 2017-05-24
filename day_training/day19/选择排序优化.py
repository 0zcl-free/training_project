array = [265, 494, 302, 160, 370, 219, 247, 287,
         354, 405, 469, 82, 345, 319, 83, 258, 497, 423, 291, 304]


def select_sort(array):
    for i in range(len(array)-1):
        smallest_index = i
        for j in range(i, len(array)):
            if array[smallest_index] > array[j]:   #smallest_index 改为i 为什么不行??
                smallest_index = j

        temp = array[i]
        array[i] = array[smallest_index]
        array[smallest_index] = temp



if __name__ == "__main__":
    print(array)
    select_sort(array)
    print(array)