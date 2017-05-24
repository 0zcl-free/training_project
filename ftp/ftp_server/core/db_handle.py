
"""
读用户数据与写用户数据
"""
import json
from conf import settings


def user_load(user_path):
    """
    读用户数据
    :param user_path:读出的路径
    :return: 用户数据字典
    """
    user_data = json.load(open(user_path, "r", encoding="utf-8"))
    return user_data


def user_dump(user_path, user_data):
    """
    将数据写到用户数据库
    :param user_path:写入的路径
    :param user_data: 要写入的数据
    :return:
    """
    json.dump(user_data, open(user_path, "w", encoding="utf-8"))