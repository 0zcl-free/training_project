
import os


def get_dirsize(dir):
    """
    获取目录的大小
    :param dir: 目录的路径
    :return: 大小(字节)
    """
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size



