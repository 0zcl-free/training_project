
import logging
from conf import settings


def log(logging_type):
    """
    main模块调用access_logger = log.log("access")
    :param logging_type: "access"
    :return: 返回logger日志对象
    """
    logger = logging.getLogger(logging_type)   #传日志用例，生成日志对象
    logger.setLevel(settings.LOGIN_LEVEL)      #设置日志级别

    ch = logging.StreamHandler()     #日志打印到屏幕，获取对象
    ch.setLevel(settings.LOGIN_LEVEL)

    # 获取文件日志对象及日志文件
    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOGIN_TYPE[logging_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOGIN_LEVEL)

    #日志格式
    formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")

    #输出格式
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    #把日志打印到指定的handler
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger      #log方法返回logger对象

    # logger.debug('debugmessage')
    # logger.info('infomessage')
    # logger.warn('warnmessage')
    # logger.error('errormessage')
    # logger.critical('criticalmessage')