# -*- coding:utf-8 -*-
import logging
from test_02.config.conf import cm


class Log():
    def __init__(self):
        self.logger = logging.getLogger()
        #创建log实例
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

        #创建实例fh用于写入到文件中设置等级为info
            fh = logging.FileHandler(cm.log_file, encoding='utf-8')
            fh.setLevel(logging.INFO)

            sh=logging.StreamHandler()
            sh.setLevel(logging.INFO)
            #创建一个格式实例
            formatter = logging.Formatter(self.fmt)
            #给两个输出器设置格式
            fh.setFormatter(formatter)
            sh.setFormatter(formatter)

            #把两个输出器连接到logger上
            self.logger.addHandler(fh)
            self.logger.addHandler(sh)

    @property
    def fmt(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'
#这些占位符都是用 %() 包围起来的，并且后面跟着一个字符，
# 表示占位符所代表的值的类型。例如，s 表示字符串类型，而 d 表示整数类型。
#每条日志记录都包含四个字段：级别、时间、位置（文件名和行号）和消息内容。
# 这些字段之间用制表符（\t）分隔。
log = Log().logger
if __name__ == '__main__':
    log.info('hello world')



