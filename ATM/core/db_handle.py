
"""
处理与数据库的交互，若是file_db_storage,返回路径
"""

def file_db_handle(database):
    """
    数据存在文件
    :param database:
    :return: 返回路径  ATM/db/accounts
    """
    db_path = "%s/%s" % (database["path"], database["name"])
    print(db_path)
    return db_path



def mysql_db_handle(database):
    """
    处理mysql数据库，这里用文件来存数据，
    保留这个方法主要为了程序拓展性
    :return:
    """
    pass


def handle(database):
    """
    对某种数据库形式处于是
    本程序用的是文件处理file_storage
    :param database: settings里面的DATABASE
    :return: 返回路径
    """
    if database["db_tool"] == "file_storage":
        return file_db_handle(database)
    if database["db_tool"] == "mysql":
        return mysql_db_handle(database)
