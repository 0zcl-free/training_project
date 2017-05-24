
def BinSearch(array, key, low, high):
    mid = int((low+high)/2)
    if key == array[mid]:  # 若找到
        return array[mid]
    if low > high:
        return False

    if key < array[mid]:
        return BinSearch(array, key, low, mid-1)
    if key > array[mid]:
        return BinSearch(array, key, mid+1, high)



if __name__ == "__main__":
    array = [4, 13, 27, 38, 49, 49, 55, 65, 76, 97]
    ret = BinSearch(array, 76, 0, len(array)-1)  # 通过折半查找，找到65
    print(ret)