
array = [219, 247, 287, 354, 405, 469, 82, 345, 319, 83, 258, 497]


def quick_sort(array):
    k = array[0]
    left_flag = 0
    right_flag = len(array)-1

    #右边小旗子开始向左移动
    while array[right_flag] > k:   #代表要继续向左移动
      right_flag -= 1
    temp = array[left_flag]
    array[left_flag] = array[right_flag]
    array[right_flag] = temp

    #左边小旗子开始向右移动
    while array[left_flag] < k:
        left_flag += 1
    #上面的loop一跳出，代表左边小旗子现在所处的位置的值在于k
    temp = array[left_flag]
    array[left_flag] = array[right_flag]
    array[right_flag] = temp



if __name__ == "__main__":
    print(array)
    quick_sort(array)
    print(array)