# encoding:utf-8

import logging
import getpass
import sys


# 定义Mylog类
class Mylog(object):
    '''这个类用于创建一个自用的log'''
    def __init__(self):
        user = getpass.getuser()
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)
        #logfile = './' + sys.argv[0][0:-3] + '.log'  # 生产日志文件名称
        logfile = 'mylog.log'
        formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')

        '''日志显示到屏幕上并输出到日志文件内'''
        loghand = logging.FileHandler(logfile)
        loghand.setFormatter(formatter)
        loghand.setLevel(logging.ERROR)    # 只记录错误

        loghandst = logging.StreamHandler()
        loghandst.setFormatter(formatter)

        self.logger.addHandler(loghand)
        self.logger.addHandler(loghandst)

        '''日志的5个级别'''

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__ == '__main__':
    mylog = Mylog()
    mylog.debug('I am debug')
    mylog.info('I am info')
    mylog.warn('I am warn')
    mylog.error('I am error')
    mylog.critical('I am critical')