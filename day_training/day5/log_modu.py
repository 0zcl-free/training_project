


import logging
# #只有比INFO级别相同或更高才写到文件
# logging.basicConfig(filename='example.log',level=logging.INFO,
#                     format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S %p')
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

print("a")
logging.warning("user [alex] attempted wrong password more than 3 times")
print('b')
logging.critical("server is down")

print("c")