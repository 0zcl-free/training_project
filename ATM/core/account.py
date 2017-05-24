
"""
用于处理用户信息的load or dump
每进行一个操作就将信息更新到数据库
"""
from core import db_handle
from conf import settings
import json

def load_account(account_id):
    """
    将用户信息从文件中load出来
    :return: 用户信息的字典
    """
    #返回路径  ATM/db/accounts
    db_path = db_handle.handle(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account_id)
    with open(account_file, "r", encoding="utf-8") as f:
        account_data =  json.load(f)
        return account_data


def dump_account(account_data):
    """
    将已更改的用户信息更新到用户文件
    :param account_data: 每操作后用户的信息
    :return:
    """
    db_path = db_handle.handle(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account_data["id"])
    with open(account_file, "w", encoding="utf-8") as f:
        json.dump(account_data, f)

    print("dump success")
