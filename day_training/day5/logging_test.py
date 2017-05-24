
import logging

# create logger
logger = logging.getLogger('TEST-LOG')  #先获取logger对象
logger.setLevel(logging.INFO)           #设置全局日志级别

# create console handler and set level to debug
ch = logging.StreamHandler()       #日志打印到屏幕，获取对象
ch.setLevel(logging.DEBUG)         #屏幕日志级别

# create file handler and set level to warning
fh = logging.FileHandler("access.log")    #先获取文件日志对象
fh.setLevel(logging.WARNING)               #文件日志级别
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter_for_file = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# add formatter to ch and fh
ch.setFormatter(formatter)      #输出格式
fh.setFormatter(formatter_for_file)

# add ch and fh to logger
logger.addHandler(ch)   #把日志打印到指定的handler
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')


