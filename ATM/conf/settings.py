
"""
初始化的配置
"""

import logging
import os

#到ATM目录，方便后面创建帐户文件
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGIN_LEVEL = logging.INFO    #初始化日志级别

LOGIN_TYPE = {
    "access":"access.log"
}


DATABASE = {
    "db_tool":"file_storage",   #文件存储，这里可拓展成数据库形式的
    "name":"accounts",          #db下的文件名
    "path":"%s/db" % BASE_DIR
}

#用户交易类型，每个类型对应一个字典，包括帐户金额变动方式，利息
TRANSACTION_TYPE = {
    "repay":{"action":"plus", "interest":0},  #存款
    "withdraw":{"action":"minus", "interest": 0.05},  #取款(提现)
    "transfer_out":{"action":"minus", "interest": 0.05}  #转帐(出)
}