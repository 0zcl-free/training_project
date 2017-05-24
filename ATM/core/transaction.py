
"""
交易模块，处理用户金额移动
"""
import json
from conf import settings
from core import account


def make_transaction(account_data, transaction_type, amount):
    """
    处理用户的交易
    :param account_data:字典，用户的帐户信息
    :param transaction_type:用户交易类型，repay or withdraw...
    :param amount:交易金额
    :return:用户交易后帐户的信息
    """
    #将字符串类型转换为float类型
    amount = float(amount)
    #如果交易类型存在
    if transaction_type in settings.TRANSACTION_TYPE:
        #利息金额
        interest = amount * settings.TRANSACTION_TYPE[transaction_type]["interest"]
        #用户原金额
        old_balace = account_data["balance"]
        print(interest,old_balace)
        #如果帐户金额变化方式是"plus"，加钱
        if settings.TRANSACTION_TYPE[transaction_type]["action"] == "plus":
            new_balance = old_balace + amount + interest
        #如果帐户金额变化方式是"minus",减钱
        elif settings.TRANSACTION_TYPE[transaction_type]["action"] == "minus":
            new_balance = old_balace - amount - interest
            #减钱时对帐户金额进行检查，防止超额
            if new_balance < 0:
                print("\033[31;1mYour Credit [%s] is not enough for transaction [-%s], and Now your"
                      " current balance is [%s]" % (account_data["credit"], (amount+interest), old_balace))
                return

        account_data["balance"] = new_balance
        #调用core下account模块将已更改的用户信息更新到用户文件
        account.dump_account(account_data)
        return account_data

    else:
        print("\033[31;1mTransaction is not exist!033[0m")
